---
channel: "Asian Dad Energy"
video_id: "grKvoLLG6bk"
title: 'The AI Coding Revolution Has a Huge Problem?'
published_at: "2026-06-24"
duration: "14:13"
word_count: 11840
---

# The AI Coding Revolution Has a Huge Problem?

[00:00] Hello world, I'm an unemployed ex-big tech software engineer with 25 years of experience in the tech industry.
[00:06] So in my involuntary early retirement, I found that being free from constant stress and deadlines, it has allowed me to rekindle my love for programming.
[00:17] It really feels like I'm a teenager again, and this led me to really try to keep up with advancements in software engineering.
[00:25] So recently I caught wind of a massive debate that's happening in the developer community, and it was caused by Boris Cherney.
[00:33] Now, Boris works at Anthropic, and he's the creator of Claude Code, which is like the most popular agentic harness on planet Earth right now.
[00:44] For the non-developers out there, you can think of an agentic harness as this type of computer program that has all of these tools and information so that it allows a large language model like ChatGPT or Claude to be able to do work on a computer rather than just answering questions from a chat window.
[01:04] So Boris is like this top dog thought leader in the software engineering space.
[01:09] Anyways, Boris sparked this massive debate by declaring on this podcast that he was on that coding is largely a solved problem.
[01:20] He mentioned that he hasn't written a single line of code since November 2025 and that all of his code is now written by Claude Code.
[01:30] This seems to suggest that agentic AI have essentially taken over coding for even the most advanced users.
[01:39] Now, I was pretty amused by some of the comments on that podcast, and it brought back memories of my first experiences with agentic orchestration at work.
[01:50] So the year was 2025.
[01:52] I had been on a months-long medical leave to take care of my sick wife, and I had just gotten back to work at my big tech job.
[01:59] Now, one of the first things that I noticed here was that my big tech employer was feverishly trying to push their own agentic harness onto all the software engineers at work.
[02:12] Apparently, our company's leadership had heard about leading agentic harnesses like Cursor and Claude Code.
[02:20] They had heard about the massive productivity gains that such tools granted.
[02:25] Supposedly, it can make an engineer a 10x engineer.
[02:28] As such, they decided that we should have our own in-house and vastly superior version of Claude Code.
[02:37] Let's call this application Kevin.
[02:40] Now, Kevin, at least to me, seems to be this slow, heavy, agentic harness with a ton of enterprise compliance guardrails.
[02:51] And it seemed only to use past-generation large language models under the hood.
[02:56] Now, I had to use Kevin at work, but I had Claude Code at home, so I can see the difference.
[03:03] But Kevin, warts and all, it was still capable of performing the crucial agentic orchestration necessary for software development.
[03:13] So, what is so important about agentic orchestration?
[03:17] Well, in just the last couple of years, the process of software engineering has shifted dramatically.
[03:23] We went from writing code manually to prompting a chatbot, essentially, for snippets of code and integrating manually those snippets of code into our code base to this concept of agentic orchestration.
[03:38] So, agentic orchestration is like this controlled coordination between a human engineer and a team of semi-autonomous AI agents.
[03:49] The goal of all this orchestration is to allow that team of AI agents to be able to design, build, test, and deploy software semi-autonomously.
[04:00] Now, there's still a man in the loop, right?
[04:03] The human engineer would provide input during the design and planning stages of the project.
[04:09] He would also be needed to review the output of the AI agents.
[04:13] And as the software is getting developed, he could be looped in if the AI agents get stuck or have any questions.
[04:21] But overall, this process should, in theory at least, allow the human engineer to produce the same amount of code for vastly less effort.
[04:31] So, the obvious benefit here is that the human engineer can 10x his productivity if this orchestration process worked.
[04:41] And in my opinion, that's really why our leadership was pushing so hard for Kevin to be adopted internally by every business unit, every internal organization.
[04:51] So, over the course of a couple of months, I used Kevin every day.
[04:57] And I observed what actually happened.
[04:59] And I saw some fundamental issues with this agentic orchestration method of software development that I want to share.
[05:07] So, let's get to it.
[05:08] So, first of all, agentic AI treats requirements as simple text rather than this interconnected pool of logic.
[05:18] And that's a real problem.
[05:20] Because the large language models inside of those agentic harnesses, they're not actually capable of logic or reasoning.
[05:29] As such, they're essentially blind to business goals and business logic unless it's meticulously documented.
[05:38] If a business requirement is not clearly documented, the AI agent could use an example from its past training data and implement something that's likely totally wrong.
[05:50] And practically speaking, we can only document requirements up to a certain level of granularity, right?
[05:58] After a certain point, it would require so much documentation that it would be less effort to just write the code ourselves.
[06:06] Thus, the sparsity of documented business domain knowledge, well, it sometimes causes AI agents to generate code that looks right on the surface.
[06:16] Like, it could pass all the syntax checks, its unit tests will succeed and work, but pretty often, that code would fail to perform the actual business logic.
[06:28] And those unit tests, a lot of times, the test doesn't actually test anything.
[06:34] Now, I remember this problem being especially prominent when the newly generated code has to integrate with legacy codebases and existing legacy systems.
[06:45] So, the context window is an AI model's short-term memory.
[06:51] And most AIs, even the most advanced ones, they have relatively small context windows.
[06:58] So, naturally, when we're working with larger codebases, the AI agents would quickly approach and exceed their context windows.
[07:07] Once that happens, the AI will start hallucinating.
[07:11] They'll begin to hallucinate API usage.
[07:14] They'll introduce deprecated libraries.
[07:16] They'll keep repeating code patterns that had already been rejected by PRs in the past, and so on.
[07:23] And I remember various colleagues using all of these tactics to mitigate this problem.
[07:30] Tactics like compacting, where you basically summarize what's in the context window to reduce the size in terms of memory.
[07:38] There's selectively excluding certain portions of the codebase from that agent's context window.
[07:45] There's the use of sub-agents to basically firewall off pieces of the business problem context from the main agent doing the work.
[07:54] But the problem is, none of these mitigation strategies actually solve the main issue.
[08:01] So, once you have your agentic pipeline set up, it could generate a ton of code, like thousands of lines of code a day, every day.
[08:11] And this generated code contains a whole lot of inefficiencies.
[08:16] AI orchestration often generates code with layers of unnecessary complexity, redundancy, almost duplicative code that's going to be difficult to maintain and upgrade.
[08:30] And without proper human supervision, this massive tidal wave of code is going to make it into production, right?
[08:37] And when that happens, it produces a host of bad outcomes: bloated repositories, a mountain of bad tech debt, and over time, an opaque black box architecture that's incredibly difficult to maintain and debug.
[08:53] Avoiding all of these problems hinges on good human supervision.
[08:58] And that leads to the biggest problem that I saw with agentic orchestration of software development.
[09:05] The human in the loop is responsible for reviewing and signing off on the output generated by the AI agents.
[09:12] But humans were made out of flesh and blood.
[09:15] So while a team of AI agents could generate thousands of lines of code an hour, an experienced human software engineer, well, he can only review several hundred lines of such code on any given day, while still maintaining a high defect detection rate.
[09:33] If for the sake of achieving that 10x productivity gain, the human engineer was forced to review thousands, even tens of thousands of lines of generated code, then cognitive fatigue would quickly set in.
[09:48] And after a short while, the engineer would lose basic comprehension of the code that he's supposed to be reviewing.
[09:55] At that point, the human reviewer simply becomes a rubber stamp.
[10:00] An accountable party on paper that cannot and should not be held accountable for that code.
[10:07] At that point, the software engineer becomes indistinguishable from just a vibe coder.
[10:13] Someone who builds software by repeatedly prompting AI until something just works.
[10:18] Someone who does not understand and is incapable of maintaining the code generated by AI.
[10:24] So yeah, those were the main issues that I saw with agentic orchestration and software development.
[10:31] Now, don't get me wrong.
[10:33] Agentic orchestration could be extremely productive in certain scenarios.
[10:38] Your smaller greenfield software projects using common language stacks like JavaScript or Python.
[10:46] I think that's really the ideal use case for agentic AI.
[10:51] In fact, I recently just used agentic orchestration to build my little micro SaaS application, Fun Employment Day, right?
[10:59] That's like a time tracking app.
[11:01] While my team of AI agents completed the design implementation and automated testing of this site in just a couple of hours, it still took me days to manually review the code and to manually test the functionality of the site.
[11:15] Now, imagine applying that same approach to a huge brownfield code base while operating under unrealistic productivity expectations from the leadership.
[11:28] Under such conditions, every weakness of agentic orchestration, well, becomes magnified.
[11:34] And no matter from which angle I approach this, the result is going to be developer burnout, developer exhaustion, and a mountain of AI generated slop code that no one can understand or even want to maintain.
[11:49] Now, that's just my opinion, right?
[11:53] But some of the top AI engineers out there, they seem to have a different perspective.
[11:58] Take Boris Cherney again, for example.
[12:01] He supposedly commits 150 PRs a day, a superhuman level of output for a software engineer.
[12:08] His latest advice is to stop prompting AI agents directly and to start building loops.
[12:14] Similarly, you got Peter Steinberger, the creator of OpenClaw.
[12:20] He recently argued that our focus should be on designing loops that prompts AI agents, rather than manually orchestrating every interaction ourselves.
[12:31] And that sent me down the rabbit hole of loop engineering, a concept where you got these autonomous AI agents that repeatedly generate, evaluate, and refine their own work.
[12:44] Now, maybe I'm just not smart enough here to get it.
[12:49] But the more I read into loop engineering, the less sense it makes to me.
[12:54] What's even more frustrating to me is that all of these giga-chad AI engineers, they haven't shared a single concrete example of how this kind of loop-based agentic orchestration works in practice.
[13:08] Not one.
[13:09] Honestly, it feels less like engineering and more like mysticism or maybe alchemy.
[13:15] So where does that leave me?
[13:17] At this point, all that I can confidently say is that agentic orchestration has got a bunch of major problems.
[13:25] And AI-powered software development, it's far from a solved problem.
[13:30] With that said, I'm going to keep experimenting and learning.
[13:34] I'm going to keep on trying to figure out this agentic AI puzzle.
[13:38] And if you're interested, you're of course welcome to come along for the ride.
[13:43] And that's all I have to say about that.
[13:45] Anyways, if you have a morbid interest to join me in this life journey, please feel free to subscribe to my YouTube channel and subscribe to my Substack newsletter.
[13:55] If you want to support me in my V-log creation efforts, please feel free to become a member of this channel or just buy me a coffee.
[14:03] If you like a one-on-one coaching session with me, just schedule it.
[14:07] Anyways, thanks so much for watching.
[14:09] Talk soon.
[14:10] Bye.