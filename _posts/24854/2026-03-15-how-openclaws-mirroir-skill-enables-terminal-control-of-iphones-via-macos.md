---
layout: post
title: "How OpenClaw&#8217;s Mirroir Skill Enables Terminal Control of iPhones via macOS"
date: 2026-03-15T20:46:17
categories: [24854]
original_url: https://insightginie.com/how-openclaws-mirroir-skill-enables-terminal-control-of-iphones-via-macos
---

How OpenClaw’s Mirroir Skill Enables Terminal Control of iPhones via macOS
==========================================================================

In a [recent GitHub update](https://github.com/openclaw/skills/blob/main/skills/skills/jfarcand/mirroir/SKILL.md), OpenClaw introduced a new skill named Mirroir that empowers users to control iPhones directly from the macOS terminal. This skill is a game-changer for developers, testers, and automation specialists who need to manage iPhone operations programmatically.

What is the Mirroir Skill for OpenClaw?
---------------------------------------

Mirroir stands as an MCP (Micro Automation Platform) server, designed to leverage iPhone Mirroring on macOS to automate tasks on an iPhone via terminal commands. It allows you to:

* Capture screenshots of the iPhone screen
* Perform taps, swipe, and type operations with precision
* Launch apps and navigate between screens
* Record videos of iPhone interactions
* Utilize OCR (Optical Character Recognition) to read on-screen text
* Run multi-step automation scenarios

When to Use the Mirroir Skill
-----------------------------

The Mirroir skill shines in scenarios where you need to interact programmatically with an iPhone. Here are some examples:

* **User Interaction Simulation:** Tap, swipe, type, and navigate through apps just like a real user.
* **Cross-Platform App Testing:** Test apps available on the App Store, TestFlight, or Expo Go, without needing their source code.
* **Automation:** Automate repetitive tasks like adding calendar events, setting reminders, or sending messages through apps like iMessage or WhatsApp.
* **UI Testing and Validation:** Capture screenshots and OCR the screen to check UI elements and flows automatically.
* **Multi-Step Workflows:** Run complex scenarios that might involve various apps and interactions.

Conditions to Avoid the Mirroir Skill
-------------------------------------

Although Mirroir is powerful, there are cases where it should not be used, including:

* **macOS-based Tasks:** When tasks can be performed entirely on macOS without the need for iPhone interaction (e.g., sending iMessages from macOSMessages.app).
* **Alternative Tools:** If there’s a better suited automation tool for macOS’s native apps, it’s often better to use those instead.
* **Missing Dependencies:** Ensure that iPhone Mirroring is connected properly before attempting to use Mirroir, as it is a prerequisite for operation.

Setup and Installation for Mirroir
----------------------------------

Before starting with Mirroir, ensure your setup meets the requirements:

* **macOS Version:** macOS 15+ (Sequoia or later)
* **iPhone Connection:** iPhone must be connected via iPhone Mirroring.
* **Software Dependencies:** Karabiner-Elements must be installed along with having Screen Recording and Accessibility permissions enabled.

Two primary installation methods stand out:

**Homebrew Installation:** A one-line command installs Mirroir using Homebrew, a common package manager for macOS:

```
/bin/bash -c "$(curl -fsSL https://mirroir.dev/get-mirroir.sh)"
```

**NPM Installation:** Alternatively, you can install Mirroir using Node.js and npm:

```
npx -y iphone-mirroir-mcp install
```

Configuring Mirroir as an MCP Server
------------------------------------

Mirroir integrates with OpenClaw as an MCP server, which means it can process commands sent from automation workflows. To configure Mirroir in OpenClaw MCP settings:

```
{
    "mirroir": {
        "command": "npx",
        "args": [
            "-y",
            "iphone-mirroir-mcp"
        ]
    }
}
```

For Homebrew installations, you can reference the binary path directly:

```
{
    "mirroir": {
        "command": "iphone-mirroir-mcp"
    }
}
```

After installation, enable system settings, especially within System Settings > General > Login Items & Extensions, to ensure the Karabiner-Elements driver is operational.

A Comprehensive Workflow with Mirroir
-------------------------------------

A typical interaction cycle with the Mirroir skill includes steps like:

1. **Checking Status:** Verify that the iPhone Mirroring connection is active with `mirroir status`.
2. **Describing the Screen:** Use OCR to identify elements on the screen and their exact coordinates with `mirroir describe_screen`.
3. **Performing Actions:** Execute commands such as tapping, typing, or launching apps by referencing the coordinates from the previous step.
4. **Verification:** Capture a screenshot or run another screen description to confirm that actions were executed correctly.

This workflow forms the foundation for automating a variety of iPhone interactions directly from the terminal.

Core Tools and Capabilities
---------------------------

Mirroir provides a comprehensive set of tools and commands designed to handle a wide array of iPhone interactions, categorized here for clarity:

* **Screen & Vision Workflow:**
  + `screenshot` – Capture the iPhone screen as a PNG file.
  + `describe_screen` – OCR the screen, while returning coordinates for touchable elements and a grid-overlaid screenshot for better identification.
* **Input Methods:**
  + `tap x y` – Tap at specific coordinates.
  + `double_tap x y` – Perform a double tap.
  + `long_press x y` – Execute a long press, typically used for context menus.
  + `swipe from_x from_y to_x to_y` – Swipe between two points on the screen.
  + `drag from_x from_y to_x to_y` – Drag an icon or apply changes by slowly moving a point.
  + `type_text "text"` – Type text using the virtual keyboard.
  + `press_key key [modifiers]` – Simulate pressing a key along with modifiers like Command, Shift, Option, or Control.
* **Recording & Measurement Functions:**
  + `start_recording` – Initiate a video recording of the iPhone screen.
  + `stop_recording` – Stop the recording and provide the file path of the saved .mov file.

Step-By-Step Execution: Sending an iMessage
-------------------------------------------

To demonstrate Mirroir’s capabilities, here’s an example of automating the process of sending an iMessage:

1. `launch_app "Messages"` — Open the Messages application.
2. `describe_screen` — Use OCR to learn the coordinates of the “New Message” button.
3. `tap [x] [y]` — Tap the identified coordinates of the “New Message” button.
4. `type_text "Bob"` — Enter the recipient’s name.
5. `describe_screen` — Use OCR again to find the recipient’s contacts within a list.
6. `tap [x] [y]` — Tap on Bob’s contact.
7. `tap [x] [y]` — Tap the message field to open the cursor.
8. `type_text "Running 10 min late"` — Type out the message you want to send.
9. `press_key return` — Press enter to send the message.
10. `screenshot` — Capture the confirmation of the sent message.

Advanced Use Cases: Recording a Bug Reproduction
------------------------------------------------

Mirroir is also a valuable tool for testing and debugging, illustrated below with a recording of a detailed bug reproduction:

1. `start_recording` — Begin capturing video.
2. `launch_app "Settings"` — Open the Settings app on the iPhone.
3. `scroll_to "General"` — Scroll down to locate the section you want to test.
4. `tap [x] [y]` — Tap to navigate to further configurations and locate the “About” section.
5. `stop_recording` — Conclude the video recording, obtaining the saved .mov file path.

Automation Using YAML Scenarios
-------------------------------

For advanced users, Mirroir supports YAML configuration files. These files can automate complex scenarios without hardcoding coordinates:

```
name: Expo Go Login Flow
app: Expo Go
description: Login to Expo Go with test credentials.
steps:
  - launch: "Expo Go"
  - wait_for: "${APP_SCREEN:-LoginDemo}"
  - tap: "${APP_SCREEN:-LoginDemo}"
  - wait_for: "Email"
  - tap: "Email"
  - type: "${TEST_EMAIL}"
  - tap: "Password"
  - type: "${TEST_PASSWORD}"
  - tap: "Sign In"
  - assert_visible: "Welcome"
  - screenshot: "login_success"
```

Using these methods, Mirroir enables precise control over on-screen elements by labeling actions and verifying steps programmatically.

Conclusion
----------

The Mirroir skill by OpenClaw succeeds in bridging the gap between terminal control and iOS device interaction. By using iPhone Mirroring under macOS, Mirroir skillfully executes tasks like app testing, automation, predictive text search, and multi-step interaction workflows, all accessible through terminal commands. With the right setup and permission validations in place, Mirroir emerges as a transformative tool in the workflows of developers and testers who frequently interact with iOS devices.

For more detailed information and additional use cases, refer to the [Mirroir documentation](https://mirroir.dev) or the [OpenClaw GitHub repository](https://github.com/openclaw/skills/blob/main/skills/skills/jfarcand/mirroir/SKILL.md).

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/jfarcand/mirroir/SKILL.md>