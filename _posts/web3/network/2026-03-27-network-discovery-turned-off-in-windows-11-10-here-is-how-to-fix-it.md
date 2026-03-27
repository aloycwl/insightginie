---
layout: post
title: Network Discovery Turned Off in Windows 11/10? Here is How to Fix It
date: '2026-03-27T00:00:31+00:00'
categories:
- web3
- network
original_url: https://insightginie.com/network-discovery-turned-off-in-windows-11-10-here-is-how-to-fix-it/
featured_image: /media/images/8146.jpg
---

<h1>Network Discovery Turned Off and Won&#8217;t Turn On in Windows 11/10: The Ultimate Fix</h1>
<p>Have you ever tried to connect to a shared printer or access files on another computer on your local network, only to find that your PC refuses to see them? You navigate to the Advanced sharing settings, click &#8216;Turn on network discovery,&#8217; hit &#8216;Save changes,&#8217; but the setting immediately reverts to &#8216;Turn off network discovery.&#8217; This is a frustratingly common issue for Windows 10 and Windows 11 users.</p>
<p>When network discovery is turned off, your computer becomes invisible to other devices, and conversely, it cannot see them. This isolation is usually a security feature, but when you actually <em>need</em> to share resources, it becomes a major roadblock. In this guide, we will walk you through the troubleshooting steps to permanently fix this issue.</p>
<h2>Why Is Network Discovery Refusing to Turn On?</h2>
<p>Before diving into the fixes, it helps to understand why Windows might be forcing network discovery to stay off. Typically, this behavior is triggered by one of the following culprits:</p>
<ul>
<li><strong>Stopped Services:</strong> The services responsible for network discovery are not running or are disabled.</li>
<li><strong>Network Profile Mismatch:</strong> Your network profile is set to &#8216;Public&#8217; instead of &#8216;Private,&#8217; and Windows restricts discovery on public networks for security.</li>
<li><strong>Firewall Interference:</strong> Your third-party antivirus or Windows Defender firewall is blocking discovery protocols.</li>
<li><strong>Corrupted Configuration:</strong> Temporary system files or registry keys related to network discovery have become corrupted.</li>
</ul>
<h2>Step-by-Step Fixes for Network Discovery Issues</h2>
<h3>1. Change Your Network Profile to Private</h3>
<p>Windows treats Public networks as untrusted, automatically disabling discovery to keep you safe in coffee shops or airports. If you are at home, ensure your network is set to Private.</p>
<ul>
<li>Open <strong>Settings</strong> and go to <strong>Network &#038; internet</strong>.</li>
<li>Click on <strong>Wi-Fi</strong> or <strong>Ethernet</strong> depending on your connection.</li>
<li>Click on the properties of your connected network.</li>
<li>Under <strong>Network profile type</strong>, select <strong>Private</strong>.</li>
</ul>
<h3>2. Check the Necessary Services</h3>
<p>Network discovery relies on a few specific Windows Services. If these are stopped, the setting cannot stick.</p>
<ol>
<li>Press <strong>Win + R</strong>, type <code>services.msc</code>, and hit Enter.</li>
<li>Locate the following services:
<ul>
<li><strong>Function Discovery Provider Host</strong></li>
<li><strong>Function Discovery Resource Publication</strong></li>
<li><strong>SSDP Discovery</strong></li>
<li><strong>UPnP Device Host</strong></li>
</ul>
</li>
<li>For each one, double-click it, set the <strong>Startup type</strong> to <strong>Automatic</strong>, and click <strong>Start</strong> if the service status is &#8216;Stopped&#8217;.</li>
</ol>
<h3>3. Allow Network Discovery Through Windows Firewall</h3>
<p>Sometimes, the Firewall rules are too restrictive. You need to ensure the protocol is allowed.</p>
<ol>
<li>Open the Control Panel and navigate to <strong>System and Security > Windows Defender Firewall</strong>.</li>
<li>Click <strong>Allow an app or feature through Windows Defender Firewall</strong>.</li>
<li>Click <strong>Change settings</strong>.</li>
<li>Scroll down to find <strong>Network Discovery</strong>. Ensure both <strong>Private</strong> and <strong>Public</strong> checkboxes are ticked (though keeping Public unchecked is safer for security).</li>
</ol>
<h3>4. Use the Command Prompt Method</h3>
<p>If the GUI keeps reverting your changes, try forcing it via the Command Prompt.</p>
<ol>
<li>Search for <strong>cmd</strong>, right-click, and select <strong>Run as administrator</strong>.</li>
<li>Type the following command and hit Enter: <code>netsh advfirewall firewall set rule group="Network Discovery" new enable=Yes</code></li>
</ol>
<h2>Advanced Troubleshooting: When Nothing Else Works</h2>
<p>If you have tried the above and still cannot turn on network discovery, you may need to look at deeper configuration issues, such as the SMB 1.0 protocol or Group Policy settings. Note that SMB 1.0 is considered insecure, so only enable it if absolutely necessary for an older device.</p>
<h2>Conclusion</h2>
<p>Resolving the issue where network discovery is turned off and won&#8217;t turn on is typically a matter of aligning your network profile type and ensuring critical background services are running. By systematically checking your settings—starting with the network profile and moving to service management—you can usually restore connectivity within minutes. If the issue persists, ensure that your third-party security software is not overriding your Windows settings.</p>
<h2>Frequently Asked Questions</h2>
<h3>Q: Is it safe to turn on Network Discovery on Public networks?</h3>
<p>A: No. It is highly recommended to keep Network Discovery turned off when connected to public Wi-Fi networks, as it exposes your computer to potential security threats from other users on that same network.</p>
<h3>Q: Why does my Windows setting keep reverting to &#8216;Turn off&#8217;?</h3>
<p>A: This usually happens because Windows detects that your network profile is set to &#8216;Public&#8217; or because a required system service failed to start properly, causing the system to revert to the safer, restricted state.</p>
<h3>Q: Do I need to restart my computer after changing these settings?</h3>
<p>A: While often not required, restarting your PC after changing services settings or firewall rules is a good practice to ensure all configurations are applied correctly.</p>
