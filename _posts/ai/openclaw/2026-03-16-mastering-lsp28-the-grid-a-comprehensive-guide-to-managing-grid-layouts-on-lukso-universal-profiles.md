---
layout: post
title: 'Mastering LSP28 The Grid: A Comprehensive Guide to Managing Grid Layouts on
  LUKSO Universal Profiles'
date: '2026-03-15T21:46:08'
categories:
- ai
- openclaw
original_url: https://insightginie.com/mastering-lsp28-the-grid-a-comprehensive-guide-to-managing-grid-layouts-on-lukso-universal-profiles/
featured_image: /media/images/8141.jpg
---

<h1>Mastering LSP28 The Grid: A Comprehensive Guide to Managing Grid Layouts on LUKSO Universal Profiles</h1>
<p>Welcome to the ultimate guide on managing grid layouts using LSP28 The Grid on LUKSO Universal Profiles. In this post, we&#8217;ll explore how to create, update, and manage grid layouts with mini-apps, iframes, and external links, offering a seamless way to enhance your Universal Profiles.</p>
<h2>Understanding LSP28 The Grid</h2>
<p>LSP28 The Grid is a powerful feature that allows you to organize and display content within your Universal Profile. By leveraging LSP28 The Grid, you can create visually appealing and interactive layouts that showcase your mini-apps, iframes, and external links in a structured manner.</p>
<h2>Getting Started with LSP28 The Grid</h2>
<h3>Configuring Your Environment</h3>
<p>Before diving into LSP28 The Grid, ensure your environment is configured correctly. Set the following environment variables:</p>
<ul>
<li><code>UP_PRIVATE_KEY</code>: Your controller&#8217;s private key.</li>
<li><code>UP_ADDRESS</code>: Your Universal Profile address.</li>
<li><code>KEY_MANAGER</code>: Your key manager address.</li>
</ul>
<h3>Creating a Grid Layout</h3>
<p>A grid layout can include mini-apps, iframes, and external links. Here&#8217;s an example of a grid layout:</p>
<pre>
const gridData = {
  isEditable: true,
  items: [
    {
      type: 'miniapp',
      id: 'app1',
      title: 'My App',
      backgroundColor: '#1a1a2e',
      textColor: '#ffffff',
      text: 'Click me'
    },
    {
      type: 'iframe',
      src: 'https://example.com/embed',
      id: 'frame1',
      title: 'External Content'
    },
    {
      type: 'external',
      url: 'https://example.com',
      id: 'link1',
      title: 'Visit Site'
    }
  ]
};
</pre>
<h2>Encoding Your Grid Layout</h2>
<p>To store your grid layout on your Universal Profile, you need to encode it as a VerifiableURI:</p>
<pre>
const jsonString = JSON.stringify(gridData);
const base64Data = Buffer.from(jsonString).toString('base64');
const verifiableUri = `data:application/json;base64,${base64Data}`;
</pre>
<h2>Executing the Transaction</h2>
<p>To update your grid layout, you&#8217;ll need to execute a transaction using your key manager:</p>
<pre>
const LSP28_GRID_KEY = '0x31cf14955c5b0052c1491ec06644438ec7c14454be5eb6cb9ce4e4edef647423';

const LSP0_ABI = [
  'function setData(bytes32 dataKey, bytes dataValue) external'
];

const LSP6_ABI = [
  'function execute(bytes calldata payload) external payable returns (bytes memory)'
];

const provider = new ethers.JsonRpcProvider('https://rpc.mainnet.lukso.network');
const wallet = new ethers.Wallet(process.env.UP_PRIVATE_KEY, provider);

const upInterface = new ethers.Interface(LSP0_ABI);
const executeData = upInterface.encodeFunctionData('setData', [
  LSP28_GRID_KEY,
  ethers.toUtf8Bytes(verifiableUri)
]);

const keyManager = new ethers.Contract(process.env.KEY_MANAGER, LSP6_ABI, wallet);
const tx = await keyManager.execute(executeData);
const receipt = await tx.wait();
console.log('Grid updated in block:', receipt.blockNumber);
</pre>
<h2>Grid Item Types</h2>
<p>LSP28 The Grid supports three types of items: mini-apps, iframes, and external links. Let&#8217;s explore each type in detail.</p>
<h3>Mini-App</h3>
<p>A mini-app is a small, interactive application that can be displayed within your grid layout:</p>
<pre>
{
  type: 'miniapp',
  id: 'unique-id',
  title: 'App Title',
  text: 'Button text',
  backgroundColor: '#fe005b',
  textColor: '#ffffff',
  size: 'medium'
}
</pre>
<h3>IFrame</h3>
<p>An iframe allows you to embed external content within your grid layout:</p>
<pre>
{
  type: 'iframe',
  id: 'unique-id',
  title: 'Frame Title',
  src: 'https://example.com/embed'
}
</pre>
<h3>External Link</h3>
<p>An external link lets you direct users to external websites:</p>
<pre>
{
  type: 'external',
  id: 'unique-id',
  title: 'Link Title',
  url: 'https://example.com'
}
</pre>
<h2>Full Grid Structure</h2>
<p>The grid layout is structured as follows:</p>
<pre>
{
  isEditable: true,
  items: [
    // Array of grid items
  ]
}
</pre>
<h2>Important Constants</h2>
<p>Here are some important constants to remember when working with LSP28 The Grid:</p>
<ul>
<li><code>LSP28_GRID_KEY</code>: <code>0x31cf14955c5b0052c1491ec06644438ec7c14454be5eb6cb9ce4e4edef647423</code> &#8211; Data key for grid storage.</li>
<li><code>Chain ID</code>: <code>42</code> &#8211; LUKSO Mainnet.</li>
<li><code>RPC URL</code>: <code>https://rpc.mainnet.lukso.network</code> &#8211; Public RPC endpoint.</li>
</ul>
<h2>Color Contrast Requirements</h2>
<p>Ensure text is readable on background colors:</p>
<ul>
<li><strong>Background</strong>: <code>#1a1a2e</code> (dark)</li>
<li><strong>Text Color</strong>: <code>#ffffff</code> (white)</li>
<li><strong>Result</strong>: Good contrast</li>
<li><strong>Background</strong>: <code>#ffffff</code> (white)</li>
<li><strong>Text Color</strong>: <code>#000000</code> (black)</li>
<li><strong>Result</strong>: Good contrast</li>
<li><strong>Background</strong>: <code>#fe005b</code> (pink)</li>
<li><strong>Text Color</strong>: <code>#ffffff</code> (white)</li>
<li><strong>Result</strong>: Good contrast</li>
<li><strong>Background</strong>: <code>#000000</code> (black)</li>
<li><strong>Text Color</strong>: <code>#fe005b</code> (pink)</li>
<li><strong>Result</strong>: Good contrast</li>
</ul>
<h2>Common Mistakes to Avoid</h2>
<p>Avoid these common mistakes when working with LSP28 The Grid:</p>
<ul>
<li><strong>Wrong property names</strong>: Use the correct property names for each item type.</li>
<li><strong>Missing required fields</strong>: Ensure all required fields are included for each item type.</li>
<li><strong>Wrong encoding</strong>: Use <code>toUtf8Bytes</code> instead of <code>toUtf8String</code> when encoding.</li>
</ul>
<h2>Transaction Flow</h2>
<p>The transaction flow for updating your grid layout involves the following steps:</p>
<ul>
<li><strong>Controller Key</strong> initiates the transaction.</li>
<li><strong>KeyManager.execute(payload)</strong> executes the transaction.</li>
<li><strong>UP.setData(LSP28_GRID_KEY, verifiableUri)</strong> updates the grid layout on your Universal Profile.</li>
<li><strong>Grid updated on-chain</strong> reflects the changes.</li>
</ul>
<h2>CLI Usage</h2>
<p>Use the provided script to update your grid layout:</p>
<pre>
# Use example grid
node scripts/update-grid.js --example

# Load from JSON file
node scripts/update-grid.js --file my-grid.json
</pre>
<h2>References</h2>
<p>For more information, refer to the following resources:</p>
<ul>
<li><a href="https://github.com/lukso-network/LIPs/blob/main/LSPs/LSP-28-TheGrid.md">LSP28 Standard</a></li>
<li><a href="references/lsp28-spec.md">Full LSP28 specification</a></li>
<li><a href="scripts/update-grid.js">Complete working example</a></li>
</ul>
<p>By following this guide, you&#8217;ll be well on your way to mastering LSP28 The Grid and creating stunning grid layouts for your LUKSO Universal Profiles. Happy coding!</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/luksoagent/lsp28-grid/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/luksoagent/lsp28-grid/SKILL.md</a></p>
