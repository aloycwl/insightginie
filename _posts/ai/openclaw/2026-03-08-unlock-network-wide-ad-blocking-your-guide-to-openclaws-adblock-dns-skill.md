---
layout: post
title: "Unlock Network-Wide Ad Blocking: Your Guide to OpenClaw&#8217;s AdBlock DNS Skill"
date: 2026-03-08T02:46:30
categories: [24854]
original_url: https://insightginie.com/unlock-network-wide-ad-blocking-your-guide-to-openclaws-adblock-dns-skill
---

[AdBlock DNS](https://github.com/openclaw/skills/blob/main/skills/skills/picaye/adblock-dns/SKILL.md) is a powerful skill for OpenClaw that provides network-wide ad and tracker blocking at the DNS level, offering a [Pi-hole](https://pi-hole.net/) alternative that runs directly on your machine. With this skill, you can block ads, trackers, malware, and telemetry domains across your entire network, protecting all your devices from intrusive ads and unwanted tracking.

What AdBlock DNS Does
---------------------

AdBlock DNS acts as a DNS sinkhole server, intercepting and blocking requests to known ad and tracker domains. By using this skill, you can enjoy ad-free browsing across all your devices, including:

* Phones
* Tablets
* Smart TVs
* Laptops
* IoT devices

AdBlock DNS leverages a comprehensive database of over 189,000 ad and tracker domains, using the same blocklists as Pi-hole, including:

* [Steven Black](https://github.com/StevenBlack/hosts)'s hosts file
* [AdAway](https://adaway.org/)
* [EasyList](https://easylist.to/)
* [EasyPrivacy](https://easylist.to/)
* [Anti-Malware](https://pgl.yoyo.org/adservers/serverlist.php)

AdBlock DNS effectively blocks ads in various formats, such as banners, tracking pixels, and in-app ads. It also prevents unwanted tracking and blocking known malware domains. However, it's essential to note that AdBlock DNS has limitations:

* It cannot block ads served from the same domain as the content, such as YouTube or Twitch ads. For these platforms, consider using a browser extension like [uBlock Origin](https://github.com/gorhill/uBlock).
* AdBlock DNS only blocks domains and cannot block in-page ad elements. To block these elements, use a browser ad blocker.
* HTTPS/DoH queries that bypass system DNS won't be caught by AdBlock DNS.

How AdBlock DNS Works
---------------------

AdBlock DNS operates on your machine, intercepting DNS queries and determining whether to block or allow them based on its comprehensive blocklist. Here's how it works:

1. When a device on your network queries a domain, the request goes to your machine running AdBlock DNS.
2. AdBlock DNS checks if the domain is on its blocklist.
3. If the domain is blocked, AdBlock DNS returns 0.0.0.0, effectively blocking the request.
4. If the domain is not blocked, AdBlock DNS forwards the query to an upstream DNS server, such as Cloudflare (1.1.1.1), for resolution.

All queries are logged, and AdBlock DNS provides statistics, including total queries, blocked percentage, and top blocked domains.

Setting Up AdBlock DNS
----------------------

To set up AdBlock DNS, follow these steps:

### Step 1: Run the Setup Script

1. Navigate to the AdBlock DNS directory:

   ```
   cd /path/to/skills/adblock/scripts
   ```
2. Run the setup script:

   ```
   bash setup.sh
   ```

This script will:

* Install the necessary dependencies.
* Create a systemd service, which runs as root, starts on boot, and auto-restarts.
* Download the blocklists (over 150,000 domains).
* Start the DNS server on port 53.
* Start a stats API on port 8053.
* Print your DNS IP and device setup instructions.

Note that you will need to enter your sudo password once during the setup process.

If you prefer not to use systemd, you can manually start the DNS server with the following command:

```
sudo node dns-server.js
```

### Step 2: Change DNS Settings on Your Devices

For AdBlock DNS to be effective, all devices on your network must use your machine's IP address as their DNS server. To do this, you'll need to configure your devices to use the IP address obtained from the setup script. Here's how to configure DNS settings for different devices:

* **Router (blocks the entire network):**

  ```
  Log into your router admin panel (usually 192.168.1.1).
  Find DNS settings (usually under DHCP or Internet/WAN settings).
  Set primary DNS to your machine's IP.
  Set secondary DNS to 1.1.1.1 (fallback if your machine is off).
  ```

  All devices on your network will now be protected.
* **iPhone/iPad:**

  ```
  Go to Settings > Wi-Fi.
  Select your network.
  Tap Configure DNS.
  Choose Manual and add your machine's IP.
  ```
* **Android:**

  ```
  Go to Settings > Network & internet > Wi-Fi.
  Select your network.
  Tap the cog icon for advanced settings.
  Set DNS to your machine's IP.
  ```
* **Mac:**

  ```
  Go to System Settings > Network > Wi-Fi.
  Click Details.
  Go to the DNS tab and add your machine's IP.
  ```
* **Windows:**

  ```
  Go to Settings > Network & internet > Wi-Fi.
  Click Hardware properties.
  Set DNS server assignment to Manual and enter your machine's IP under IPv4 DNS.
  ```
* **Linux:**

  ```
  Edit /etc/resolv.conf or NetworkManager:
  nmcli con mod "Wi-Fi" ipv4.dns "MACHINE_IP"
  ```

Refer to the documentation provided in the setup script for specific instructions tailored to your device and network configuration.

### Step 3: Verify That AdBlock DNS Is Working

To ensure AdBlock DNS is functioning correctly, perform the following tests using nslookup or check the API:

1. Using nslookup: Open a terminal on your machine and run the following commands:

   ```
   nslookup ads.google.com MACHINE_IP
   Should return 0.0.0.0 (blocked)

   nslookup google.com MACHINE_IP
   Should return a real IP (allowed)
   ```
2. Using the API: Run the following command to check the statistics:

   ```
   curl http://localhost:8053/stats
   ```

   This command will display the total queries, blocked queries, block percentage, and top blocked domains.

Agent Commands
--------------

If you're using AdBlock DNS in an automated or programmatic context, you can leverage the following commands to interact with AdBlock DNS:

### Check Stats

To view the statistics provided by AdBlock DNS, run the following command:

```
curl -s http://localhost:8053/stats | python3 -m json.tool
```

### Whitelist a Domain

If a website or service is not functioning correctly due to AdBlock DNS blocking a required domain, you can whitelist the domain with the following command:

```
curl -s -X POST http://localhost:8053/whitelist/add -H "Content-Type: application/json" -d '{"domain":"example.com"}'
```

Replace `example.com` with the domain you want to whitelist.

### Block a Specific Domain

If you want to add an additional domain to the blocklist, use the following command:

```
curl -s -X POST http://localhost:8053/blacklist/add -H "Content-Type: application/json" -d '{"domain":"annoying-site.com"}'
```

Replace `annoying-site.com` with the domain you want to block.

### Check if a Domain Is Blocked

To determine whether a specific domain is blocked by AdBlock DNS, run the following command:

```
curl -s "http://localhost:8053/check?domain=ads.google.com"
```

Replace `ads.google.com` with the domain you want to check.

### Update Blocklists

Blocklists are automatically updated every 24 hours. To force an update, use the following command:

```
curl -s -X POST http://localhost:8053/update
```

This command will immediately update the blocklists with the latest information.

### View Whitelist

To view the list of whitelisted domains, run the following command:

```
curl -s http://localhost:8053/whitelist
```

Running AdBlock DNS as a Service
--------------------------------

The `setup.sh` script automatically configures AdBlock DNS to run as a service. If you need to manage the service manually, use the following commands:

* Start:

  ```
  sudo systemctl start adblock-dns
  ```
* Stop:

  ```
  sudo systemctl stop adblock-dns
  ```
* Restart:

  ```
  sudo systemctl restart adblock-dns
  ```
* Check status:

  ```
  sudo systemctl status adblock-dns
  ```
* View logs:

  ```
  journalctl -u adblock-dns -f
  ```
* Remove completely:

  ```
  sudo systemctl disable adblock-dns
  sudo rm /etc/systemd/system/adblock-dns.service
  sudo systemctl daemon-reload
  ```

Configuration
-------------

AdBlock DNS stores its configuration in `data/config.json`. You can edit this file to customize the behavior of AdBlock DNS:

```
{
  "upstream": "1.1.1.1",
  "port": 53,
  "apiPort": 8053
}
```

The available settings are:

* `upstream`: The upstream DNS server used to resolve non-blocked domain queries (e.g., Cloudflare, Google 8.8.8.8).
* `port`: The DNS port used by the server (port 53 is the standard DNS port and requires sudo).
* `apiPort`: The port used by the stats API.

Conclusion
----------

[AdBlock DNS](https://github.com/openclaw/skills/blob/main/skills/skills/picaye/adblock-dns/SKILL.md) is a powerful tool for blocking ads and trackers at the DNS level, providing network-wide protection for all your devices. With its easy setup process and comprehensive blocklists, AdBlock DNS offers an effective [Pi-hole](https://pi-hole.net/) alternative that runs directly on your machine. By following the steps outlined in this guide, you can enjoy ad-free browsing and enhanced network privacy.

To learn more about AdBlock DNS, visit the [OpenClaw skills](https://github.com/openclaw/skills/tree/main/skills/skills/picaye/adblock-dns) repository on GitHub.

[Source: GitHub](https://github.com/openclaw/skills/blob/main/skills/skills/picaye/adblock-dns/SKILL.md)

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/picaye/adblock-dns/SKILL.md>