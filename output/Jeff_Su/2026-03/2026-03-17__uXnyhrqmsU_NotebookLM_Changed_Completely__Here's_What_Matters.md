---
channel: "Jeff Su"
video_id: "_uXnyhrqmsU"
title: 'NotebookLM Changed Completely: Here''s What Matters (in 2026)'
published_at: "2026-03-17"
duration: "20:30"
word_count: 22506
---

# NotebookLM Changed Completely: Here's What Matters (in 2026)

[00:00] Notebook LM, after receiving a massive amount of updates recently, is now more popular than even Gemini in terms of usage and interest, which is pretty wild.
[00:08] So if you're still using Notebook LM like you were a few weeks ago, you're missing out on some incredible capabilities.
[00:14] In this video, I cover what Notebook LM is still the best at, then go through the features and the workflows that actually matter.
[00:21] Let's get started.
[00:22] Even with all the updates, Notebook LM's core advantage has not changed.
[00:26] Here's a simple illustration.
[00:27] Three different health insurance providers send you their coverage options.
[00:31] The first one gives you a PDF brochure, the second gives you a spreadsheet, and the third recorded a video walkthrough.
[00:37] Instead of digging through all that dense material, you throw them into Notebook LM and ask something like, which provider offers the best dental coverage?
[00:44] And Notebook LM parses through everything to give you a grounded answer.
[00:48] In other words, Notebook LM is still the perfect tool when three things are true.
[00:52] One, you already know which documents or files contain the answers, and you just need help getting through them.
[00:58] Two, those sources are in different formats, like PDFs, spreadsheets, and slides, or different mediums, text, audio, video.
[01:06] And no single one gives you the full picture.
[01:09] Three, you need the AI to stick to what's actually in the documents and not make things up, because the stakes are too high for hallucinations.
[01:15] Jumping into the app, I'm in an empty Notebook right now, and as you can see, there's a simple three column layout.
[01:21] And the way to use this is to simply go from left to right.
[01:24] One, two, three.
[01:25] Starting off with the sources panel on the left, this is where you add everything Notebook LM needs to work with, PDFs, slides, audio recordings, spreadsheets, you name it.
[01:34] You're basically telling Notebook LM, the answers are in here somewhere.
[01:38] Moving onto the chat panel in the middle, this is where you interact with your sources by asking questions, requesting summaries, or pulling out specific details.
[01:46] And all the way to the right, the studio panel.
[01:48] This is where we generate actual deliverables that we can use in the real world, things like reports and slide decks.
[01:53] We're gonna spend most of our time here today.
[01:55] To quickly recap, first, we load in everything we're working with on the left.
[01:59] Then we uncover insights in the middle.
[02:01] And on the right, we turn all of that into something we can actually use.
[02:05] Next, let's walk through the sources panel with a real example.
[02:08] At Google, I had to build a proposal on increasing Gemini usage in the Asia Pacific region.
[02:13] So I create a Notebook and add two sources I already have, an internal strategy document and a PDF with regional data.
[02:19] But I'm still missing some market specific data.
[02:22] So I select the web plus fast research combination within the discover sources field and type top five AI models by usage in the Japan market with monthly active users for each model, hit enter.
[02:34] And while it's running, the rule of thumb is to treat the web plus fast research combination as Google search without leaving Notebook LM.
[02:42] Notebook LM returns a list of sources for me to review.
[02:44] So let's open this up.
[02:45] And my rule of thumb is to select three sources maximum, because it forces me to actually go in and check each source.
[02:54] And so that acts as a built-in quality filter.
[02:57] After reading through the results, I've decided to add these three.
[03:00] And you'll notice one of them is in Japanese, a language I definitely can't speak.
[03:04] But pro tip, you can still add it because Notebook LM can pull out the relevant information and answer your questions in English.
[03:12] Moving on, you want to treat the drive plus fast research combination like the Google Drive search bar.
[03:18] For example, I can type something like find that report with the AI model statistics on the Japan market. since I remember the Japan team actually sent me something a while back.
[03:27] And I can find the file like this without having to dig through my drive.
[03:31] I can also tell Notebook LM to find that start on Android slide deck from the global team, because I want to reference their structure when building out my own presentation.
[03:42] And there it is.
[03:44] Now, the web plus deep research combination.
[03:46] I'll ask for a report on LLM model usage by country in Asia, and I'll fast forward this part.
[03:52] As you can see, the biggest difference is that deep research finds sources and synthesizes them into a full research report you can add as a source, along with a list of sources it pulled from.
[04:02] Put simply, fast research gives you a list of sources to manually review.
[04:06] Deep research takes the extra step of reading those sources and writing a report for you.
[04:10] While that sounds great in theory, I don't recommend using deep research here, because number one, if you have any domain expertise on the topic, you can probably filter out low quality sources better than Notebook LM.
[04:20] And number two, the deep research tools in Gemini, ChatGPT, and Claude will just perform better.
[04:27] Pro tip number one, if you add Google docs and slides or sheets as sources, they're treated as living documents, meaning we can fetch the latest changes from those files.
[04:36] So for example, if someone adds new slides to the startup Android deck, I can click to sync the latest version.
[04:42] So it's updated by the next time I query this notebook.
[04:46] PDFs, on the other hand, are static uploads.
[04:49] So keep that in mind.
[04:50] Pro tip number two, for websites that cannot be added as a source directly, as you can see, it's highlighted in red here.
[04:55] We can go to that website, right click, open up reading mode, highlight all the text here, then paste it back into Notebook LM under the copied text selection.
[05:07] So to recap, we started with two sources we already had, then use the discover sources function to fill in what we were missing.
[05:14] And now we have everything we need to work with.
[05:17] Moving over to the chat panel in the middle.
[05:19] The most important feature here is the configure chat window.
[05:22] For a high stake tasks, you always want to add a custom instruction.
[05:26] So every response in this notebook is framed around your specific goal.
[05:30] What I usually do is go over to Gemini and paste in this prompt template.
[05:34] I'll leave a link down below.
[05:35] I need a custom instruction for a Notebook LM notebook, blah, blah, blah.
[05:39] The goal of this notebook is you insert your end goal here.
[05:41] And for this example, I'm just going to paste what I have, develop a business proposal for increasing Gemini's monthly active users.
[05:47] I'm going to let this run.
[05:49] I then copy Gemini's output here and paste it back into my notebook.
[05:55] And now every response from Notebook LM is filtered through that lens.
[05:59] And I usually leave the response length on default, since I can always ask Notebook LM to expand later on.
[06:05] Next, after I've had a few back and forths with this notebook, I want to go up here and click delete chat history before I start a completely new conversation so the AI isn't influenced by my previous conversations.
[06:18] But before I delete, I check if there's anything worth keeping.
[06:21] For example, if there's a useful data point I know I'll refer to again, I'll save this as a note.
[06:27] Or if it's a really important insight, I can take this a step further by turning that note into a source.
[06:35] So it gets factored into every future studio output.
[06:39] Pro tip, if you click into any source, you'll see a source guide at the top.
[06:43] And I found this to be incredibly useful after adding in a dense source, and you're not sure where to start.
[06:49] For example, here, I see that Gemini is rapidly growing in India, thanks to massive telecom partnerships and Android integration.
[06:57] And that immediately gives me a follow-up question.
[07:00] Why aren't we replicating this telecom partnership strategy in Indonesia, Pakistan, and Japan?
[07:09] And that's something I wouldn't have asked without the source guide surfacing it first.
[07:15] Now, earlier I mentioned that if you want to use deep research, you're better off doing it in Gemini directly.
[07:20] Today's sponsor, HubSpot, actually put together a free guide that maps out exactly how that works.
[07:25] From running deep research in Gemini, to importing the results into Notebook LM, to generating deliverables from everything combined.
[07:31] My favorite part about this guide is that it breaks the workflow down across 11 specific use cases, like marketing strategy, customer research, and actually something I've used myself, the competitive intelligence program, each with its own step-by-step instructions.
[07:45] So you're not guessing how to adapt the process to your role.
[07:47] The guide is completely free, so I'll leave a link down below.
[07:50] Thank you HubSpot for sponsoring this video.
[07:52] Now we get to the really fun part.
[07:53] The studio panel has received the most updates, and it's the main reason Notebook LM has evolved from a Q&A chatbot to a production tool.
[08:01] Here's a simple visualization.
[08:02] Before, you would upload your sources, ask Notebook LM something like, "How did we do this year compared to last year?"
[08:08] Copy that answer and paste it into a separate document.
[08:11] Now Notebook LM skips that middle step and generates the report directly.
[08:15] Not every tool here is equally useful though, so I've split them into Tier 1 must-used and Tier 2 situational tools.
[08:21] First up, Reports lets you go from raw sources to a finished briefing doc or competitive analysis in minutes, instead of spending hours outlining and drafting it yourself.
[08:30] Clicking on Reports, you'll see default format options up here, which I skipped because they're pretty generic.
[08:35] And instead, I focus on the suggested formats down here, because these are dynamic.
[08:40] Notebook LM has analyzed all our sources and suggested the most useful directions to take, so we don't waste time brainstorming.
[08:47] Clicking into the Competitive Positioning Analysis format, we see that Notebook LM has auto-generated a tailored prompt for us that helps us identify opportunities for winning over enterprise clients and mobile-first consumer segments.
[08:59] Okay.
[09:00] I didn't write this prompt, right?
[09:01] Notebook LM inferred it from my sources.
[09:04] Here's another example.
[09:05] I've uploaded my company's bank statements into this notebook.
[09:08] I click Reports, and none of the suggested formats actually match what I want.
[09:13] So I click Create Your Own, and instead of writing a custom instruction from scratch, I'd head on back to Gemini, and I paste this prompt template, which I'll link below.
[09:22] And I just need to provide two inputs, the purpose of the report and who the report is for.
[09:27] I copy and paste Gemini's output back into the custom instructions field here, which tells Notebook LM I want a breakdown of my finances and areas to save money.
[09:38] Click Generate, and within a few minutes, I'm just going to fast forward here.
[09:43] I have a pretty comprehensive report with everything I asked for.
[09:46] Moving on, the Slide Deck tool builds you a complete presentation directly from your sources, but there's a catch.
[09:52] It's not easy to edit the final output.
[09:54] Here's how it works.
[09:55] In this notebook, I have a bunch of sources related to my Workspace Academy course, from marketing materials to course scripts.
[10:00] And when I click on the Slide Decks tool, I can choose Presenter Slides, which generates visual slides meant to be presented, or Detailed Deck, which produces a self-contained deck meant to be read without a speaker.
[10:13] We'll go with the Detailed option for this example, leave the length on default, and guide the notebook with a custom instruction.
[10:20] Create a deck designed to pitch my course to enterprise clients.
[10:22] Use action-oriented headlines and three talking points maximum for each slide.
[10:27] And we're going to let this generate.
[10:28] Now, the output is pretty damn good.
[10:30] Let's expand this.
[10:31] Okay.
[10:32] Nice.
[10:34] Okay.
[10:34] Wow.
[10:35] It even created a wireframe of Google Drive to illustrate how this course applies the parent method.
[10:40] That's awesome.
[10:41] But if you download this as a PowerPoint, you'll actually realize when you open it up, that all these slides are images and not editable elements.
[10:52] Does that make this tool useless?
[10:54] Of course not.
[10:55] An extremely underrated use case is having notebook.lm propose a presentation narrative to cut down the amount of time we spend on brainstorming.
[11:03] For example, my boss tells me to put together a narrative for the Google I/O keynote this year.
[11:07] I can upload all the information I know I need to include and use the slide deck tool to generate a detailed deck first, just to see what narrative it proposes.
[11:17] Now, I have a starting point to work on.
[11:21] Okay.
[11:21] Let's expand this out.
[11:23] The visuals look great and it seems like the narrative starts at a high level, then dives into specific projects, case studies, and products, which makes sense.
[11:35] And let's say we need to make some edits because this looks pretty good from a narrative standpoint.
[11:39] Let's go back to the first slide.
[11:40] I can click the revised button here to start leaving editing instructions on individual slides.
[11:45] So for this slide, I feel like the key visual on the right is way too complicated.
[11:49] Let's remove all the text and simplify the visual.
[11:52] And this slide is fine.
[11:55] Let's just give one more example here.
[11:56] Use Google brand colors because this is not the Google blue.
[12:01] And we're going to click generate new deck.
[12:03] All right.
[12:03] After a couple of minutes, we have entirely new deck with the changes applied.
[12:06] As you can see, the key visual here is simplified.
[12:09] There's no more text.
[12:10] Awesome.
[12:11] And we're using the Google brand colors here.
[12:13] Pretty cool, right?
[12:14] Once everything is finalized, we can click the three dots and we can choose to download as PDF or PowerPoint.
[12:20] But by the time you're watching this, maybe we'll be able to export to Google slides as well.
[12:25] Pro tip.
[12:25] You can also use slide decks to generate vertical carousel slides for social media.
[12:30] Instead of the default horizontal format, we're going to open up slide deck.
[12:34] And under the custom prompts, we're going to add a prompt specifying a vertical slide deck in 9 to 16 portrait format that's optimized for mobile screens.
[12:43] And I've already prepared the output here.
[12:45] This is still technically a set of slides, but we can download it as a PDF and attach directly to our LinkedIn or Instagram posts.
[12:54] Speaking of social media, the infographic tool turns your sources into a single polished visual you can post or send out right away.
[13:00] Back in the Google I/O notebook, I want to create an infographic promoting the event, obviously.
[13:05] And for orientation, I'm going to choose one by one square dimension.
[13:08] And I am going to select the instructional visual style.
[13:13] For level of detail, just avoid detailed because this has the most text typos.
[13:18] I'm going to go with concise for this.
[13:20] And I'm just going to type top five takeaways for Gemini Enterprise, use Google brand colors, and we're going to click generate.
[13:25] And after a minute, I have a pretty on-brand visual and it's pretty clean that I can just post on LinkedIn along with a totally non-cringy and non-corporate BSE post to extend the event's reach.
[13:36] Pro tip, if you have a specific brand guideline, upload it as a source and add, follow the attached brand guideline for colors, fonts, and design style, and notebook.lm will match the infographic to your branding.
[13:47] Pro tip, this applies to reports and slide decks as well.
[13:51] Just upload your guideline, reference it in your custom instructions, and all three tools stay on-brand.
[13:57] Moving on, the mind map tool shows you everything in your sources at a glance, so you know exactly what's worth digging into before you read a single page.
[14:05] For instance, when I was preparing for my last ChatGPT video, I added a bunch of sources I know I'll need, but there's no point reading through all of it since most of it won't make it into a 10-minute video.
[14:15] But after generating a mind map, I can instantly see every topic and, clicking to these arrows, subtopics laid out visually, and cherry-pick the ones my viewers would actually benefit from.
[14:27] For example, this branch, 11 practical techniques, I immediately know it's worth exploring further, versus something like agentic toggles, API tips, right?
[14:35] Since this would be too technical for my audience.
[14:38] And because mind maps are interactive, I can click on any of these nodes, for example, 11 practical techniques, and it opens a chat grounded in my sources about that specific topic.
[14:49] So I go from a bird's-eye view of everything to a focused conversation about one subtopic in a single click.
[14:56] By the way, if you want to boost your Google workspace productivity by 1% every week, including Gemini tips, you can sign up for my weekly newsletter.
[15:03] Every issue is a bite-sized tip you can read and apply in under 60 seconds.
[15:07] Link down below.
[15:08] Moving on, Tier 2 tools are a bit more situational, so I won't go as deep into each one.
[15:13] But if you have an underrated use case, let me know in the comments.
[15:15] Data tables are useful when you need to pull scattered information from your sources into a structured table you can sort and filter.
[15:22] In this notebook, I've uploaded pricing pages and feature lists of the top AI models, and I can ask Notebook.lm, after clicking into the data table tool, to generate a competitor comparison table with these columns, pricing, key features, etc., right?
[15:36] And since I've already prepared this ahead of time, I'm just going to expand this.
[15:39] And as you can see, a table is generated, and I can even click the three dots here to export to Google Sheets directly.
[15:45] Or let's say I want to review my marketing campaign performance.
[15:47] I upload historical data from previous campaigns that might be scattered across different formats, right?
[15:52] Then upload my latest campaign data, and Notebook.lm generates a clean side-by-side comparison in minutes.
[15:59] Pro tip, other AI tools like Gemini and ChatGPT can generate tables as well, obviously.
[16:04] But since Notebook.lm is grounded in our sources, I trust the answers from Notebook.lm significantly more.
[16:10] The video overview tool turns your sources into a short narrated slideshow with simple visuals, which is great when you want to watch something instead of read.
[16:18] Case in point, I'm a big fan of Ben Thompson's long-form interviews, but I don't want to read through 20 to 30 pages of text.
[16:26] So I just upload the transcript onto Notebook.lm and click into video overview, select the detailed explainer format, and select the whiteboard visual style.
[16:36] This is just personal preference.
[16:37] And then I just ask for a breakdown of the top five arguments from the interview.
[16:41] After 10 to 15 minutes, these take a while to generate.
[16:44] Notebook.lm condensed that entire interview into its main arguments.
[16:48] Let's play a few seconds from this.
[16:50] Evan says that to understand the present, you have to look at the past.
[16:53] And right now, we are in a phase of destruction before creation.
[16:57] And I found the visuals to really help me understand the concepts, as opposed to audio overviews, which I'll touch on in a bit.
[17:03] Now, Google recently upgraded video overviews with a cinematic mode, and here's the difference.
[17:08] The standard video overview is basically audio on top of a slideshow, whereas cinematic video overviews use Google's VO video model to generate actual animated sequences with fluid motion.
[17:21] So it's closer to a short explainer video than a narrated slide deck.
[17:25] And since it's limited to ultra subscribers for now, I'm not going to go too deep into it right now.
[17:30] The quiz tool generates a set of multiple choice questions grounded in your sources.
[17:34] And I found this surprisingly useful for live events.
[17:37] So I Google for both internal town halls and external workshops.
[17:40] I upload the speaker presentations, generate a quiz with multiple choice questions, then use Slido or Mentimeter to add an interactive element to the event without having to ask speakers to provide questions themselves.
[17:52] The flashcards tool helps us memorize key terms, concepts, or facts from our sources.
[17:57] So it's great for certification exam prep.
[18:02] But it's been a while since I took a test like the GMAT.
[18:05] But if I were preparing for this, I'd upload the prep materials here.
[18:09] Click into the quiz.
[18:09] Level difficulty, click hard because I super smart Asian.
[18:13] Let's leave the prompt empty and you can watch me kill these questions.
[18:18] What is the definition of an irrational number?
[18:20] Easy, a number that's not rational.
[18:22] Next.
[18:23] Which should be written as infinite, non-repeating decimal.
[18:27] No, that's wrong.
[18:29] All right, moving on to audio overviews.
[18:31] I'll be very honest.
[18:32] This has mainly been a gimmick for me because every use case it's supposedly good for, like deep dive, brief, critique, or debate, I can get to the same result faster by asking a question in chat and reading its answer.
[18:45] And taking this a step further, if I actually wanted like a solid critique on one of my deliverables, like a proposal, I would actually use Gemini because Gemini will reason for longer and actually give me creative recommendations.
[18:58] Notebook LM is not good for this.
[19:00] All that said, I do use it for longer newsletters I can't be bothered to read.
[19:04] I would turn those into audio overviews and actually listen to it on my Notebook LM mobile app while I'm commuting or cleaning.
[19:11] All right, I obviously can't go through every single use case in one video.
[19:14] So here's a quick lightning round of notebooks I keep coming back to.
[19:17] First up, health reports.
[19:19] I upload my health reports each year and ask Notebook LM to flag anything that's changed significantly from last year and highlight trends I should watch over time.
[19:26] Second, meeting notes knowledge base.
[19:28] I keep meeting transcripts that are automatically generated by Gemini in a notebook so that before any meeting I can just ask targeted questions and I can trust the answers because they're grounded in the meeting notes themselves.
[19:42] Third, tax and accounting.
[19:43] I upload my financial statements along with the tax code and now I can ask things like what deductions am I eligible for based on my income and expenses.
[19:51] Here's something most Notebook LM users forget though.
[19:53] Notebook LM's biggest strength, high accuracy, is also its biggest limitation, low creativity, since those two dimensions are inherently linked.
[20:02] Put another way, if your task requires more creativity, like brainstorming ideas, drafting creative copy, or writing code, you need a tool like Gemini, ChatGPT, Claude, or Grok.
[20:12] And to Google's credit, they found a way to have their cake and eat it too by integrating Notebook LM within Google Gemini.
[20:19] But this video is already obviously too long, so let me know in the comments if you want a standalone video on that.
[20:23] You can check out my Gemini tutorial here.
[20:25] See you on the next video and in the meantime, have a great one.