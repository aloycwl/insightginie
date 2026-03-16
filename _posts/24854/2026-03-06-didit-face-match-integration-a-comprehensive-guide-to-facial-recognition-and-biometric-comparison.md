---
layout: post
title: "Didit Face Match Integration: A Comprehensive Guide to Facial Recognition and Biometric Comparison"
date: 2026-03-06T16:17:51
categories: [24854]
original_url: https://insightginie.com/didit-face-match-integration-a-comprehensive-guide-to-facial-recognition-and-biometric-comparison
---

What is Didit Face Match?
-------------------------

Didit Face Match is a powerful standalone API that enables developers to compare two facial images and determine if they belong to the same person. This skill integrates the Didit Face Match functionality into your applications, providing a similarity score between 0-100 to help you make informed decisions about identity verification.

### Key Features and Capabilities

The Didit Face Match skill offers comprehensive facial comparison capabilities:

* **Similarity Scoring**: Returns a numerical score (0-100) indicating how similar the two faces are
* **Age Estimation**: Provides estimated age for detected faces in both images
* **Gender Detection**: Identifies the gender of detected faces
* **Face Bounding Boxes**: Returns coordinates for face locations in the images
* **Configurable Decline Threshold**: Set your own acceptance criteria with customizable thresholds
* **Image Rotation Support**: Automatically rotates images to find upright faces
* **Multi-Face Detection**: When multiple faces are present, the largest face is selected for comparison

Technical Specifications and Requirements
-----------------------------------------

Understanding the technical requirements is crucial for successful implementation:

### Supported Image Formats

The API supports the following image formats:

* JPEG
* PNG
* WebP
* TIFF

### File Size Limitations

Each image must be under 5MB in size. This limitation ensures optimal processing speed and accuracy while maintaining reasonable bandwidth usage.

### Face Selection Logic

When an image contains multiple faces, the system automatically selects the largest face for comparison. This approach typically identifies the primary subject in group photos or images with multiple people.

Authentication and API Key Management
-------------------------------------

Secure authentication is essential for using the Didit Face Match API. Here’s how to obtain and manage your API credentials:

### Getting Your API Key

You can obtain your API key through two methods:

#### Method 1: Business Console

1. Log in to your Didit Business Console

2. Navigate to API & Webhooks section

3. Generate or copy your existing API key

#### Method 2: Programmatic Registration

If you don’t have a Didit account yet, you can create one programmatically with just two API calls:

```
# Step 1: Register
curl -X POST https://apx.didit.me/auth/v2/programmatic/register/ \
  -H "Content-Type: application/json" \
  -d '{"email": "you@gmail.com", "password": "MyStr0ng!Pass"}'

# Step 2: Verify email (check your inbox for OTP code)
curl -X POST https://apx.didit.me/auth/v2/programmatic/verify-email/ \
  -H "Content-Type: application/json" \
  -d '{"email": "you@gmail.com", "code": "A3K9F2"}'
```

The verification response will include your API key.

### Managing Credits and Billing

Didit operates on a credit-based system. To add credits:

```
# Check current balance
curl -X GET https://apx.didit.me/v3/billing/balance/ \
  -H "x-api-key: YOUR_API_KEY"

# Add credits (creates Stripe checkout link)
curl -X POST https://apx.didit.me/v3/billing/top-up/ \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"amount_in_dollars": 50}'
```

API Endpoint and Request Structure
----------------------------------

The Didit Face Match API endpoint is:

```
POST https://verification.didit.me/v3/face-match/
```

### Required Headers

```
x-api-key: YOUR_API_KEY
Content-Type: multipart/form-data
```

### Request Parameters

All parameters are sent as multipart/form-data:

| Parameter | Type | Required | Default | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| user\_image | file | Yes | — | JPEG/PNG/WebP/TIFF, max 5MB | User’s face image to verify |
| ref\_image | file | Yes | — | Same as above | Reference image to compare against |
| face\_match\_score\_decline\_threshold | integer | No | 30 | 0-100 | Scores below this = Declined |
| rotate\_image | boolean | No | false | — | Try 0/90/180/270 degree rotations |
| save\_api\_request | boolean | No | true | — | Save in Business Console Manual Checks |
| vendor\_data | string | No | — | — | Your identifier for session tracking |

Implementation Examples
-----------------------

### Python Implementation

```
import requests

response = requests.post(
    "https://verification.didit.me/v3/face-match/",
    headers={
        "x-api-key": "YOUR_API_KEY"
    },
    files={
        "user_image": ("selfie.jpg", open("selfie.jpg", "rb"), "image/jpeg"),
        "ref_image": ("id_photo.jpg", open("id_photo.jpg", "rb"), "image/jpeg"),
    },
    data={
        "face_match_score_decline_threshold": "50"
    }
)

print(response.json())
```

### JavaScript (Node.js) Implementation

```
const fs = require('fs');
const FormData = require('form-data');
const fetch = require('node-fetch');

const formData = new FormData();
formData.append('user_image', fs.createReadStream('selfie.jpg'));
formData.append('ref_image', fs.createReadStream('id_photo.jpg'));
formData.append('face_match_score_decline_threshold', '50');

const response = await fetch('https://verification.didit.me/v3/face-match/', {
    method: 'POST',
    headers: {
        'x-api-key': 'YOUR_API_KEY'
    },
    body: formData
});

const result = await response.json();
console.log(result);
```

Understanding the Response
--------------------------

A successful response (200 OK) returns comprehensive information about the face comparison:

```
{
  "request_id": "a1b2c3d4-...",
  "face_match": {
    "status": "Approved",
    "score": 80,
    "user_image": {
      "entities": [
        {
          "age": 27.63,
          "bbox": [40, 40, 100, 100],
          "confidence": 0.717,
          "gender": "male"
        }
      ],
      "best_angle": 0
    },
    "ref_image": {
      "entities": [
        {
          "age": 22.16,
          "bbox": [156, 234, 679, 898],
          "confidence": 0.717,
          "gender": "male"
        }
      ],
      "best_angle": 0
    },
    "warnings": []
  },
  "created_at": "2025-05-01T13:11:07.977806Z"
}
```

### Response Status Values

The API returns three possible status values:

* **Approved**: Score >= threshold – Faces match, proceed with confidence
* **Declined**: Score < threshold or no face detected - Check warnings for details
* **In Review**: Needs manual review – Wait for review or retrieve via session API

### Interpreting the Score

The similarity score ranges from 0-100 and should be interpreted as follows:

* **90-100**: Very high confidence – Same person (auto-approve)
* **70-89**: High confidence – Likely same person (approve at default threshold)
* **50-69**: Moderate – Possible match (consider manual review)
* **30-49**: Low – Likely different people (declined at default threshold)
* **0-29**: Very low – Different people (declined)

Warning Tags and Error Handling
-------------------------------

The API provides detailed warnings to help you understand the results:

### Auto-Decline Warnings

These warnings automatically result in a declined status:

* **NO\_REFERENCE\_IMAGE**: Reference or face image missing
* **NO\_FACE\_DETECTED**: No face detected in one or both images

### Configurable Warnings

These warnings depend on your threshold settings:

* **LOW\_FACE\_MATCH\_SIMILARITY**: Score below threshold – potential identity mismatch

### Common Error Responses

Understanding error codes helps with troubleshooting:

| Code | Meaning | Action |
| --- | --- | --- |
| 400 | Invalid request | Check file format, size, parameters |
| 401 | Invalid API key | Verify x-api-key header |
| 403 | Insufficient credits | Top up at business.didit.me |

Security Best Practices
-----------------------

Handling biometric data requires careful consideration of security and privacy:

### Data Minimization

Only store the status and score in your database. Minimize biometric image data on your servers to reduce liability and comply with privacy regulations.

### Image URL Expiration

In workflow mode, image URLs expire after 60 minutes. This automatic expiration helps prevent unauthorized access to sensitive biometric data.

### Compliance Considerations

Ensure your implementation complies with relevant regulations such as GDPR, CCPA, or other regional privacy laws that may apply to biometric data processing.

Practical Use Cases
-------------------

The Didit Face Match skill is versatile and can be applied to various scenarios:

### Identity Verification

Compare a user’s selfie with their government-issued ID photo to verify identity during account creation or high-value transactions.

### Access Control

Implement facial recognition for secure access to buildings, systems, or restricted areas by comparing live images with stored profiles.

### Age Verification

Use the age estimation feature to verify that users meet age requirements for age-restricted products or services.

### Duplicate Detection

Prevent duplicate accounts by comparing new user photos against existing database entries.

### Customer Onboarding

Streamline KYC (Know Your Customer) processes by automating document verification with facial comparison.

Utility Scripts and Advanced Usage
----------------------------------

The Didit Face Match skill includes utility scripts to simplify common tasks:

### Command Line Interface

```
# Basic comparison
export DIDIT_API_KEY="your_api_key"
python scripts/match_faces.py selfie.jpg id_photo.jpg

# With custom threshold and rotation
python scripts/match_faces.py selfie.jpg id_photo.jpg --threshold 50 --rotate
```

### Batch Processing

For processing multiple comparisons, you can create batch scripts that loop through image pairs and store results in a database for later analysis.

### Integration with Workflows

The skill can be integrated into larger verification workflows using the didit-verification-management skill for comprehensive platform management, including session handling, user management, and billing.

Performance Optimization Tips
-----------------------------

To get the best results from the Didit Face Match API:

### Image Quality

Ensure images are well-lit, in focus, and show the face clearly. Avoid sunglasses, masks, or extreme angles that might affect recognition accuracy.

### Consistent Conditions

When comparing images, try to maintain consistent lighting, background, and facial expressions between the reference and comparison images.

### Threshold Calibration

Adjust the decline threshold based on your specific use case and risk tolerance. Higher thresholds provide more certainty but may reject legitimate matches.

### Rotation Feature

Enable the rotate\_image option when dealing with images that might not be perfectly upright, as this can significantly improve match accuracy.

Conclusion
----------

The Didit Face Match skill provides a robust, easy-to-integrate solution for facial recognition and biometric comparison. With its comprehensive feature set, flexible configuration options, and strong security practices, it’s an excellent choice for developers looking to implement identity verification and face matching capabilities in their applications.

By following the guidelines and best practices outlined in this guide, you can successfully integrate Didit Face Match into your systems and provide reliable, secure facial recognition functionality to your users.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/rosasalberto/didit-face-match/SKILL.md>