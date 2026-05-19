---
channel: "Jeff Su"
video_id: "4wvLHFgnQZQ"
title: 'Top 5 Claude Cowork Tips I Wish I Knew from Day One'
published_at: "2026-05-19"
duration: "17:50"
word_count: 17040
---

# Top 5 Claude Cowork Tips I Wish I Knew from Day One

[00:00] My cowork is insanely powerful, but there's a problem.
[00:03] Right now, there's no gold standard on how to set up your workspace.
[00:06] So if you get the foundation wrong, you're gonna keep running into avoidable issues down the line.
[00:11] So after five months of using cowork daily to run my entire life and going to debt to pay for token usage, here are five essential things to get right from day one.
[00:19] Let's get started.
[00:20] Kicking things off with tip number one, the markdown translator.
[00:23] As you know by now, cowork's instructions and memory live in these .md markdown files.
[00:28] And although we can open them up and edit this directly, opening this just costs 20 tokens.
[00:34] Okay, that's a joke, but I kind of feel it's true.
[00:36] It's a pain to read like this, right?
[00:39] And annoying as hell to edit.
[00:40] So first, what you wanna do is to install a free app called Obsidian.
[00:43] Open folder as vault, open.
[00:45] Point it to your cowork workspace folder, open.
[00:49] And now every .md file instantly renders with proper headings, bold text, and bullet points.
[00:55] Basically a much more readable format.
[00:58] And now let's say I wanna change something in this claw.md file.
[01:01] Instead of doing anything here, I can select the claw.md tab in Obsidian and replace this first bullet point, for example, under preferences with always make inappropriate jokes.
[01:13] And let's just remove that line from earlier.
[01:18] And I'm gonna close this and reopen.
[01:22] And you will see that the changes are already there.
[01:27] To be clear, you don't need to learn Obsidian or use any of its other features.
[01:30] It's just a lens to read and edit .md files.
[01:35] Pro tip, you can click command and control plus to zoom in.
[01:37] You can click the reading mode icon to lock the Obsidian page so you don't make edits by mistake.
[01:43] And you can even go to Obsidian settings, files and links.
[01:47] Keep the show all file types toggle turned on.
[01:51] And this lets you see non .md files like spreadsheets, PDFs, and even images in the sidebar.
[01:59] Moving on to tip number two, the 300 line rule.
[02:01] Because a root claw.md loads every single session, a bloated file wastes a lot of tokens.
[02:06] And when I cut mine from over 600 lines to around 250, my token usage dropped by roughly 25%.
[02:14] And here are three tactics you can use right away.
[02:16] First, only include the bare essentials.
[02:18] My claw.md template has six sections.
[02:21] First, this memory system section tells Cowork to always read memory.md at session start so it knows what we did before.
[02:28] Next, preferences is how we want Cowork to communicate.
[02:32] Tone, length, format, et cetera.
[02:35] Next, rules represent behavioral guardrails.
[02:37] Basically, if you want Cowork to always do something, like always ask clarified questions before starting a complex task, or never do something, like never edit files in my workspace without telling me what you changed and why, those belong here.
[02:51] Heading over to my actual claw.md, the routing map contains a table that Cowork checks to figure out which workstation to load based on my task.
[03:02] So if I'm writing an email, we load the email HQ workstation.
[03:05] If I'm working on Chinese projects, load China desks.
[03:08] If I'm brainstorming, use Clarity Partner, so on and so forth.
[03:12] Coming back to the lightweight template since it's less dense, the fifth section, references include one-line pointers to files Cowork loads on demand.
[03:20] In other words, this voice principles.md file does not load every session, right?
[03:25] Only when I'm writing content.
[03:27] And finally, creating new workstations basically tells Cowork how to create new workstations in your workspace.
[03:34] Pro tip, the rule of thumb is to keep your claw.md file between 200 and 250 lines, with 300 being the absolute maximum.
[03:41] You can also grab these claw.md and memory.md templates from my free Cowork toolkit linked down below.
[03:47] But Jeff, I hear you say, there's no way I can keep everything within 300 lines if I keep using Cowork.
[03:53] And that brings us to tactic number two, ask Cowork to relocate non-essential rules.
[03:58] Here's the test.
[03:59] Does Cowork need this every session or only when a specific task comes up?
[04:03] Back in my actual claw.md, there's a section called Governance MISI Principle that says all instructions and rules in this workspace must be mutually exclusive and collectively exhaustive.
[04:14] And since this governs how all rules are organized in my entire Cowork workspace, this must be kept in my root claw.md.
[04:23] In contrast, there's a file creation rule bullet point down here that only apply when I'm creating a new file.
[04:28] And since I'm not creating files every session, instead of having all 22 rules live here, I have a pointer.
[04:35] Read this before creating any new file in the workspace.
[04:40] Now, let's apply this learning immediately.
[04:42] Going back to the creating new workstations section from before, we don't create new workstations every session, right?
[04:48] So, we can tell Cowork, move the creating new workstation section out of my root claw.md into a new reference file and replace it with a one-line pointer in my references table.
[04:58] And we're just gonna let this run.
[04:59] And after a few seconds, we can see what happened.
[05:02] First, even Cowork tells us that doing this keeps the root claw.md leaner while preserving the template for on-demand loading, right?
[05:09] And opening the obsidian view, we can see that the entire creating new workstation section has been removed.
[05:16] Instead, it's been replaced by a pointer.
[05:18] Hey, read this when creating a new workstation.
[05:22] And where does this workstation template .md live?
[05:26] Under the 00 resources folder.
[05:29] And as you can see, everything has been moved over here and our claw.md just got shorter without losing anything.
[05:35] It's that simple when it comes to optimizing your claw.md.
[05:38] Find sections that serve specific tasks and ask Cowork to relocate them.
[05:42] Tactic number three, write files in the right place.
[05:45] In a nutshell, most Cowork users put claw.md content in memory.md and vice versa.
[05:50] And this confusion tanks output quality.
[05:54] The solution is adding a rule under claw.md's memory system section.
[05:58] Test one, if the entry is prescriptive and contains words like always and never, then it belongs in claw.md.
[06:06] Test two, if it describes a fact that could change, then it goes into memory.md.
[06:12] Scrolling down to the rule section, here we have an entry that says, before drafting a new email, check if a related thread already exists with that recipient.
[06:19] This is a version of before doing X, do Y, which is prescriptive behavior as well, right?
[06:25] That's why it belongs in claw.md.
[06:27] Flipping over to the memory.md file and scrolling down, we see an entry here that says, my company uses Microsoft Copilot, which is something that could change tomorrow, right?
[06:36] Probably something that should change.
[06:38] Just kidding.
[06:38] So this is a temporary fact and not a rule and that's why it belongs in memory.md.
[06:44] Here's something you can do right now.
[06:45] Tell Cowork to review my root claw.md and memory.md.
[06:49] In the claw.md file, flag any entry whose primary purpose is recording a fact or status rather than prescribing how you should behave, right?
[06:57] And in memory.md, flag any entry whose primary purpose is telling you how to behave rather than recording a fact.
[07:03] Recommend where each flagged entry should move.
[07:06] And after a minute or two, Cowork will share a list of recommendations and here you can actually see there are five issues in my memory.md file which obviously I left them in there
[07:17] on purpose to show you what not to do.
[07:18] I don't make mistakes.
[07:19] And luckily my claw.md is clean though so I can just literally say proceed with changes and it's as easy as that.
[07:28] Speaking of optimizing our workspace, today's sponsor HubSpot put together a free resource called the Cloud Cowork Stack that contains 12 Cowork
[07:35] optimized prompts you can use right away.
[07:37] There are a couple I found pretty useful like this batch document generator one and the research synthesis one this one although I'd still probably use
[07:45] Cloud Web for research but my favorite by far surprise surprise is this file management prompt.
[07:50] The one change I'd make to this is instead of choosing a primary sort by date or by project tell it to organize following Tiago Forte's paramethod projects, areas,
[07:59] resources, and archive.
[08:00] That way every file lands in a bucket based on how actionable it is not just what it looks like.
[08:05] This actually inspired me to create a schedule task in Cowork that processes my iCloud inbox folder every morning meaning Cowork
[08:12] sorts through the receipts PDFs random downloads I capture into the right folder automatically.
[08:17] You can grab the Cloud Cowork stack for free link down below.
[08:20] Thank you HubSpot for sponsoring this video.
[08:22] All right tip number three the memory diet.
[08:24] Just like your root claw.md your root memory.md also loads every single session so a messy one
[08:30] wastes tokens and makes Cowork's output worse.
[08:33] So here are three things you can do.
[08:35] First give your memory.md a clear structure.
[08:37] My root memory.md has three sections with the first being active projects and work which is
[08:42] a list of everything I'm currently working on with a short status next to each one.
[08:46] So Cowork immediately knows what's on my plate.
[08:49] Second a schedule task section that tracks all my automated recurring jobs so Cowork
[08:54] doesn't doesn't accidentally create duplicates or miss a task that already exists.
[08:59] And third the core memory section stores persistent facts about me like my career
[09:03] before becoming a full-time YouTuber my LinkedIn URL and my business address and how it's
[09:08] used basically facts I need to reference all the time.
[09:11] Tactic number two set a hard ceiling so remember how in my
[09:15] root claw.md I have a memory system section and at the bottom here
[09:19] there's actually a pointer to the full set of memory
[09:23] system rules and if I open up that file there
[09:27] are two things you should know first under entry format
[09:30] there's a rule that says one to two sentences max for every memory
[09:34] entry meaning Cowork writes concise entries from day one instead of
[09:39] long paragraphs that bloats your memory.md file and wastes tokens
[09:42] next under size ceiling section there's a rule that reads root memory.md
[09:47] 150 line ceiling when the ceiling is breached the fix
[09:51] is always compression and archiving never raising the ceiling in
[09:56] plain English this means when your memory.md file inevitably reaches
[10:00] 150 lines Cowork will automatically archive information that's no longer current
[10:06] like things that happened two or three months ago but
[10:08] wait a minute where does that archived information go tactic
[10:12] number three create and archive .md here's a simple visualization your
[10:17] memory.md is a whiteboard that contains active projects and key facts you need to
[10:21] reference every day your archive.md is the filing cabinet with a complete
[10:26] record of everything you've done and here's a key insight
[10:30] Cowork does not read archive.md every session it's only when
[10:34] you ask something like what happened with the e-list three
[10:37] months ago does it then check the archive.md file to
[10:41] find the answer and because archive.md isn't loaded at session start it doesn't
[10:47] need to have a size ceiling right you can preserve everything you want without
[10:50] paying any token cost to help you set this up
[10:53] I have a prompt linked linked below that you can
[10:55] paste directly into Cowork like so in the interest of
[10:58] time I won't read the whole thing but basically this
[11:02] prompt first creates your archive.md file then adds the memory
[11:06] rules to your claw.md and teaches Cowork which entries to
[11:11] keep in memory.md and which to archive pro tip you
[11:15] want to create a separate memory.md for each workstation and
[11:18] each project like what's going on with my latest email
[11:25] campaign Cowork first checks root memory.md to see the project
[11:29] exists then jumps to the project memory.md to read project
[11:34] specific information like notion pages email subject lines past decisions
[11:38] and current status and this cascading setup is why my root
[11:42] memory.md has never gone above 100 lines even after months
[11:46] of aggressive daily use next up tip number four the
[11:49] project transplant a lot of you asked about the relationship
[11:52] between Claude projects and Cowork and long story short you
[11:55] want to migrate all your Claude projects into Cowork because
[11:59] Cowork doesn't face the same limitations as Claude projects for
[12:02] instance I used to rely on this Claude project to
[12:05] write my weekly newsletter and within this project we have
[12:08] project instructions over here a project knowledge file and auto
[12:12] generated project memory compared to Cowork there are quite a
[12:15] few problems here for example if I wanted to make
[12:18] improvements to the project instructions I would have to manually
[12:21] click in and type out something or paste in something
[12:24] right second clicking into the project memory we see it's
[12:28] an AI generated paragraph I can't really structure or edit
[12:32] directly this doesn't work really well and third even though
[12:35] I can either I have to like open the document
[12:44] and paste everything myself all these issues can be addressed
[12:47] by migrating our Claw projects into co-work and the process
[12:50] is simple the project instructions essentially become the workstation claw.md
[12:54] file project memory becomes the memory .md file and knowledge
[12:58] files get added to the project resources folder here's what
[13:02] to do in practice open up a blank text document
[13:04] go in and select all copy the project instructions and
[13:08] paste it into this document press enter twice go back
[13:13] click into project memory select all of this add a
[13:18] header one project memory paste the project memory in as
[13:23] well save this as a markdown document project info .md
[13:29] save all right and then I can download my entire
[13:34] Google doc as a markdown file as well all tabs
[13:38] this might take a few moments I might fast forward
[13:41] this in the meantime though let's head on over to
[13:43] my free template this is linked again link down below
[13:47] copy this simple migration prompt paste it into co-work and
[13:53] then back in my downloads share both the project info
[13:57] .md and my google doc md file into co-work and
[14:02] just let this run in order for the claw project
[14:05] to be migrated into co-work all right it's done let's go over
[14:09] what co-work just did first it created a newsletter workstation
[14:12] folder my newsletter is called workspace essentials but this is
[14:14] a newsletter workstation folder second second it created a workstation
[14:19] claw .md file that contains the same workflow as the
[14:23] original project instructions third it created a memory .md file
[14:27] with labeled instructions that I can actually edit like so
[14:32] and fourth it created a resources folder with three separate
[14:38] resource files one for audience and positioning one for my
[14:42] recent newsletters and one that extracted style patterns from my
[14:47] existing newsletters as a bonus we can even go back to
[14:50] our root claw .md file and scrolling all the way
[14:52] down you can see that under routing map co-work even
[14:56] added a new entry that maps to our newly created
[15:00] newsletter workstation now whenever I want to make a change to any
[15:03] of those files I can simply tell co-work hey add
[15:06] a rule to my newsletter workstation each edition should have
[15:09] a maximum of three emojis and co-work will make the
[15:12] change directly in the newsletter claw.md file as you can see
[15:16] right here and let's say I just publish the latest
[15:19] issue I can tell co-work to add the latest edition
[15:23] to the newsletter examples file paste in the copy let it run
[15:28] and after a minute I'm not going to wait I'm too
[15:31] impatient it will by the way if you want my
[15:48] complete system with pre-built workstation templates and a step-by-step walkthrough so you
[15:52] can skip the trial and error of building from scratch I'm
[15:55] putting together a co-work academy course and can sign up
[15:58] for the wait list down below moving on to tip
[16:00] number five the skill check a lot of you asked
[16:02] about skills versus workstations after my last video so here's
[16:05] the difference in a nutshell back in my actual co-work
[16:08] workspace I say I want to work on my next
[16:10] native weekly newsletter what do I need to do again
[16:12] and let's see what it says alright as you can
[16:16] see co-work first loaded my newsletter workstation for context then
[16:19] laid out the workflow but notice how a lot of these
[16:22] steps surfaces a decision I need to make for example
[16:25] step need to make decisions and judgment calls as part
[16:39] of the process in contrast once a newsletter draft is
[16:43] finalized I can trigger my newsletter subject line skill which
[16:48] takes the final draft applies the instructions from the skill
[16:52] that can run on autopilot since it's just a checklist
[16:56] and I'm going to fast forward a bit here it'll give me
[16:59] five scored options I know exactly what I'm getting back
[17:03] every time and the only thing that changes is the
[17:06] content example number two I have a workstation audit skill
[17:10] that checks for misplaced rules bloat and gaps within a
[17:13] specific workstation folder to keep my workstations optimized and lean
[17:17] the output is a report with an executive summary up
[17:19] front followed by specific findings and recommendations so the test
[17:24] for when to create a workstation versus a skill is
[17:26] actually pretty simple is this a place I work or
[17:29] a thing I do if it's an ongoing area of
[17:33] work with its own voice and accumulated context that's a
[17:36] workstation if it's a repeatable process you want done the
[17:39] same way every time that's a skill if you found
[17:42] this helpful check out my full co-work playlist next see
[17:45] you there and In the meantime, have a great one.