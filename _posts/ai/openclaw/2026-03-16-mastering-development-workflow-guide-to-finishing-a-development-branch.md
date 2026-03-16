---
layout: post
title: 'Mastering Development Workflow: Guide to Finishing a Development Branch'
date: '2026-03-16T16:46:17'
categories:
- ai
- openclaw
original_url: https://insightginie.com/mastering-development-workflow-guide-to-finishing-a-development-branch/
featured_image: /media/images/8154.jpg
---

<article>
<h1>Mastering Development Workflow: Guide to Finishing a Development Branch</h1>
<p>When working on a development project, reaching the point where you need to integrate your work back into the main codebase can be a crucial step. The <strong>Finishing a Development Branch</strong> skill is designed to streamline this process, ensuring that your implementation is complete, all tests pass, and you have clear options for integrating your work.</p>
<h2>Overview</h2>
<p>This skill guides the completion of development work by presenting structured options for merging, creating pull requests, or cleaning up. The core principle is to verify tests, present options, execute the chosen workflow, and clean up. The process begins with an announcement: <em>&#8220;I&#8217;m using the finishing-a-development-branch skill to complete this work.&#8221;</em></p>
<h2>The Process</h2>
<h3>Step 1: Verify Tests</h3>
<p>Before presenting any options, it&#8217;s essential to verify that all tests pass. This step ensures that your implementation is stable and ready for integration. The skill runs the project&#8217;s test suite using common commands like <code>inpm test</code>, <code>cargo test</code>, <code>pytest</code>, or <code>go test ./...</code>.</p>
<p>If tests fail, the skill will report the number of failures and display the errors. It will not proceed to the next step until all tests pass. This ensures that only stable code is integrated back into the main branch.</p>
<h3>Step 2: Determine Base Branch</h3>
<p>The skill identifies the base branch by checking common branches like <code>main</code> or <code>master</code>. If it cannot determine the base branch, it will ask for confirmation. For example: <em>&#8220;This branch split from main &#8211; is that correct?&#8221;</em></p>
<h3>Step 3: Present Options</h3>
<p>The skill presents four clear options for integrating your work:</p>
<ol>
<li>Merge back to the base branch locally</li>
<li>Push and create a Pull Request</li>
<li>Keep the branch as-is (you&#8217;ll handle it later)</li>
<li>Discard this work</li>
</ol>
<p>The skill asks: <em>&#8220;Which option?&#8221;</em> and expects a concise response without additional explanation.</p>
<h3>Step 4: Execute Choice</h3>
<p>Based on the chosen option, the skill executes the appropriate workflow.</p>
<h4>Option 1: Merge Locally</h4>
<p>Switch to the base branch, pull the latest changes, merge the feature branch, and verify tests on the merged result. If tests pass, delete the feature branch. Then, clean up the worktree.</p>
<h4>Option 2: Push and Create PR</h4>
<p>Push the branch to the remote repository and create a Pull Request using <code>gh pr create</code>. The skill generates a title and body for the PR, including a summary and test plan. Then, clean up the worktree.</p>
<h4>Option 3: Keep As-Is</h4>
<p>Report that the branch is being kept as-is and that the worktree is preserved. The skill does not clean up the worktree for this option.</p>
<h4>Option 4: Discard</h4>
<p>Confirm the deletion of the branch, all commits, and the worktree. The skill requires typed confirmation (<em>&#8220;discard&#8221;</em>) before executing. After confirmation, switch to the base branch, delete the feature branch, and clean up the worktree.</p>
<h3>Step 5: Cleanup Worktree</h3>
<p>For Options 1, 2, and 4, the skill checks if the worktree is used and removes it. For Option 3, the worktree is kept.</p>
<h2>Quick Reference</h2>
<table>
<thead>
<tr>
<th>Option</th>
<th>Merge</th>
<th>Push</th>
<th>Keep Worktree</th>
<th>Cleanup Branch</th>
</tr>
</thead>
<tbody>
<tr>
<td>1. Merge locally</td>
<td>✓</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>✓</td>
</tr>
<tr>
<td>2. Create PR</td>
<td>&#8211;</td>
<td>✓</td>
<td>✓</td>
<td>&#8211;</td>
</tr>
<tr>
<td>3. Keep as-is</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>✓</td>
<td>&#8211;</td>
</tr>
<tr>
<td>4. Discard</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>✓ (force)</td>
</tr>
</tbody>
</table>
<h2>Common Mistakes and Red Flags</h2>
<p>It&#8217;s crucial to avoid common pitfalls when using this skill:</p>
<ul>
<li>Never proceed with failing tests.</li>
<li>Never merge without verifying tests on the result.</li>
<li>Never delete work without confirmation.</li>
<li>Never force-push without an explicit request.</li>
</ul>
<p>Always verify tests, present clear options, get typed confirmation for discarding work, and clean up the worktree only for Options 1 and 4.</p>
<h2>Integration</h2>
<p>This skill is called by other workflow skills like <strong>subagent-driven-development</strong> and <strong>executing-plans</strong>. It pairs well with the <strong>using-git-worktrees</strong> skill, which creates worktrees that this skill cleans up.</p>
<p>By mastering the <strong>Finishing a Development Branch</strong> skill, you can ensure that your development work is completed efficiently and integrated smoothly into the main codebase.</p>
</article>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/zlc000190/finishing-a-development-branch/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/zlc000190/finishing-a-development-branch/SKILL.md</a></p>
