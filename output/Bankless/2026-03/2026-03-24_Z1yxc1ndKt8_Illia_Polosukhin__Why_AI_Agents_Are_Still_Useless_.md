---
channel: "Bankless"
video_id: "Z1yxc1ndKt8"
title: 'Illia Polosukhin: Why AI Agents Are Still Useless (And What Fixes Them)'
published_at: "2026-03-24"
duration: "1:19:19"
word_count: 77995
---

# Illia Polosukhin: Why AI Agents Are Still Useless (And What Fixes Them)

[00:00] So one thing that people don't realize, when they use Entropic, OpenAI, or even worse, you use something else for inference, OpenClaw actually sends all your secrets to those services as well.
[00:12] Yeah.
[00:13] So somewhere in Entropic and OpenAI logs, they have everybody's access keys, API keys, and bearer tokens to access your Gmails and your Notions.
[00:25] It's actually insane that we're doing that.
[00:27] Yeah.
[00:29] Ironclaw fixes that, like the keys never touch LLM.
[00:32] Bankless Nation, we are joined by Ilya Pulisukin, the co-founder of NIR.
[00:40] Ilya, welcome to Bankless.
[00:41] Thanks for having me.
[00:42] So Ilya, you are one of the eight co-authors of the Transformer paper, the famous paper, Attention is All You Need.
[00:49] The thing that kind of just broke open the doors of AI research to turn into some of the products that we know today, Chachi Boutique, Claude, et cetera.
[00:57] And then in 2017, you left Google where you were an AI researcher writing this paper to go co-found NIR.
[01:04] Question for you.
[01:05] Do you regret leaving AI to go into crypto?
[01:09] Well, the story was that I left Google to start NIR AI, which was an AI company.
[01:16] We were teaching machines to code, which is a fancy way to say vibe coding.
[01:21] And in 2017, everybody thought we were somewhere between delusional and doing science fiction at work.
[01:26] When I would go and tell people, no, no, machines will write all the code.
[01:30] Like, don't worry about it.
[01:31] People wouldn't believe me.
[01:33] And we were too early, right?
[01:35] That was a real, real challenge.
[01:38] And so what we were trying to do at the time was trying to get a lot more training data.
[01:43] And so we had students around the world, Eastern Europe, China, Southeast Asia, who were doing small tasks, small coding tasks for us to generate training data for us.
[01:53] And we had challenge paying them, right?
[01:56] You know, students in China don't have bank accounts.
[01:59] They have WeChat pay.
[02:00] Eastern Europe, every country has its own, some kind of restrictions.
[02:05] And so crypto was a pretty natural, actually, like, solution we needed for our own problem.
[02:11] It's like, hey, how do we actually pay people globally without, like, setting up a ton of entities without, you know, needing to do all the kind of hard payment provider work?
[02:20] And crypto seemed like a solution, like, hey, you know, you don't need a bank.
[02:25] You don't need a, yeah, an entity in every country.
[02:29] You can just send people money on the internet.
[02:33] But this was already 2018, there was nothing that would, like, scale work, you know, in a simple and a cheap way, right, to do this for, you know, we were paying 15 cents per task to people.
[02:45] And so that's kind of how we got into near blockchain.
[02:49] And so I would say at a time it made a little sense because it was clearly that to us at blockchain was kind of a part of the story for kind of AI evolution.
[03:02] And at the same time, like, hardware, the scale of AI itself wasn't there for what we were trying to do.
[03:08] When you wrote Attention is All You Need, how soon did you think LLMs would actually, like, happen?
[03:17] Because within five years, we had sort of the famous ChatGPT moment.
[03:21] I think that was maybe ChatGPT 3 in 2022, kind of first release.
[03:26] And that's when the world started taking notice that this thing was huge, this thing was impactful, this thing could scale.
[03:33] So that was five years later.
[03:34] Did you think it would happen on that timeline?
[03:36] Or what was your sense for where AI would go after you published the paper in 2017?
[03:42] Yeah.
[03:44] So, I mean, the reason why we started Near AI in 2017 is because we thought it's going to happen, like, right now at the time, right?
[03:50] So we actually were way more optimistic, thinking that we're almost there, right?
[03:55] We are on, like, kind of the curve we're seeing right now, we thought we were on that curve in 2017, 2018.
[04:02] And we were wrong.
[04:02] So, I mean, the main part was the compute wasn't there.
[04:07] Like, there was not enough, like, the individual and kind of cluster compute parts just weren't there.
[04:13] I think as soon as that kind of crossed the chasm, that's when this model started to scale.
[04:18] When you said that the blockchain component of AI was obvious all the way back in 2017, when you founded Near AI, people are now just starting to wrap their heads around the intersection of AI blockchain, like, today, for the first time.
[04:37] Well, what did you see all the way back in 2017 about, like, why blockchains and AI go together?
[04:42] What made sense to you back then?
[04:43] I mean, there was a few components.
[04:45] Obviously, we started with this data labeling, crowdsourcing.
[04:48] I mean, think of scale AI, right?
[04:50] Scale AI has, you know, subentities everywhere.
[04:52] It's like a thousands of people company, which then employs, you know, hundreds of thousands of people to actually do the work.
[04:59] Like, that's just a smart contract, right?
[05:02] We actually have Near Crowd been running since 2021.
[05:05] It has zero employees.
[05:07] It's, you know, employed thousands of people around the world doing crowdsourcing, right?
[05:12] So the reality is, like, a lot of the supporting infrastructure is just some forms of marketplaces that blockchain is really well designed for.
[05:22] Same for hardware, compute.
[05:25] But as you kind of progress forward and you imagine these AI systems are becoming the interface, and so, like, kind of my main thesis is AI will be the way we interface computing.
[05:38] So it will be the operating system, right?
[05:41] This was my thesis with Near AI.
[05:42] I said, I was saying back then, in 2017, that, like, hey, computers will write all the code, which means the operating system and apps are going to be just replaced by this AI that's yours, that is just writing all the code.
[05:58] And one of the implications is, like, okay, well, that kind of removes a lot of, like, SaaS and a bunch of other components, but you still need kind of how my AI and talks to your AI, how they, you know, identify each other, et cetera.
[06:13] So you kind of need to upgrade a lot of the core networking infrastructure for this world where it can fake a lot of stuff.
[06:21] You know, you obviously have, like, real civil resistance.
[06:23] We're already seeing this with AI.
[06:25] You need, you know, micropayments for actually, like, exchanging services that, again, doesn't rely on credit cards and other things.
[06:33] And so, kind of, as you go down the, like, service architecture that current operating systems use, a lot of it breaks with AI.
[06:41] And so you kind of need to fix it.
[06:42] And blockchain just have all the pieces figured out, or at least has tools to figure out how to solve that.
[06:50] Some exciting news.
[06:51] We are launching a new podcast to help people figure out the crypto cycle, how to navigate it.
[06:56] The best crypto cycle investor I know, his name is Michael Nato.
[06:58] He runs the DeFi Report.
[07:00] This is the guy that sent me a sell alert before the 1010 price drop happened.
[07:04] His cycle analysis has been absolutely on point.
[07:07] I've been following him for years.
[07:08] And this year, we started recording weekly podcast episodes.
[07:12] Each one, we get into his portfolio, what he's holding, the market structure, entry targets, fair market value of Bitcoin and Ether, and where we are in the cycle.
[07:20] There's new episodes that are released every Wednesday.
[07:22] They're 30 minutes.
[07:23] They're short.
[07:24] They're punchy.
[07:24] I think this crypto cycle is harder to navigate than most.
[07:27] So let's do it together.
[07:28] Go subscribe to this podcast.
[07:30] Search the DeFi Report wherever you get your podcasts.
[07:32] YouTube, Apple, Spotify, or find the link in the show notes.
[07:36] There's a new episode waiting for you now.
[07:37] Why does managing investments still mean juggling multiple apps, accounts, and currencies?
[07:42] Crypto trades around the clock.
[07:43] Stocks, ETFs, and commodities are moving on-chain.
[07:46] Yet most platforms still keep everything split apart, turning diversification into unnecessary friction.
[07:51] BitGet is delivering a different kind of experience with its universal exchange.
[07:55] One platform where users can access crypto, tokenized stocks, ETFs, and other assets in the same place, all traded directly using USDT.
[08:03] No constant transfers, no currency conversions, just a single account built for how markets actually move today.
[08:09] As the line between crypto and traditional finance continues to blur, BitGet's goal is straightforward.
[08:13] Make trading and investing simpler, not more complicated than it needs to be.
[08:17] Learn by clicking the link in the show notes.
[08:18] This is not investment advice.
[08:20] I want to pull on this thread that AI represents the new interface.
[08:24] So right now, I'm looking at you inside of my Chrome browser, which is running on Windows 10.
[08:29] I'm a Windows guy.
[08:30] These are the options.
[08:32] I'm sorry.
[08:33] You've lost 60% of bank listeners now.
[08:38] Unsubscribe.
[08:39] Ignoring that.
[08:44] I go back and forth.
[08:45] I also have a Mac, which maybe doesn't help me at all.
[08:48] But like there's these two operating systems, the both, you know, the Chrome browser, Windows 10, maybe I'm on a Mac and looking into you while I'm on the road, I'm on a Mac.
[08:55] Are these the operating systems that you're talking about that AI will just like replace?
[09:00] But actually for like the end consumer, how would you illustrate this?
[09:04] Yeah, I think it will start small, right?
[09:08] And, you know, we see this as open claw, iron claw type products, and we can talk about this.
[09:13] I think where the final will be like your phone just comes in with AI, right?
[09:19] And like it boots into the AI operating system.
[09:21] And that AI operating system, you know, it pulls whatever pieces it needs.
[09:25] It composes the software you need.
[09:26] It, you know, generates the software to record podcasts.
[09:31] You know, on the back end, it'll connect to my agent, you know, it will schedule time for us.
[09:36] So it's just Siri.
[09:38] My new, my new iPhone comes in and only Siri is loaded and Siri can do anything.
[09:42] Don't say Siri.
[09:43] Siri is so dumb, David.
[09:44] Yeah, let's call it Jarvis or something.
[09:45] Sure.
[09:46] Yeah, like imagine, you know, you load up into the suit and it's like, clearly Tony Stark didn't build all of the software Jarvis built it.
[09:54] So that's, that's kind of the experience, right?
[09:57] So if AI is the interface, then everything you described in kind of blockchain and crypto are these parts of the services.
[10:05] So services will still exist in some form.
[10:08] And I guess financial services, you know, all of the different money verbs will exist in some form.
[10:13] It's like blockchain and crypto, a financial and property rights service for AI.
[10:20] How do you, how do you think about all of the other pieces that AI will actually need apart from the user interface?
[10:25] Yeah.
[10:26] I mean, I usually say AI is a user interface, blockchain is a backend, right?
[10:30] Okay.
[10:30] So, um, yeah, so what, what do you actually need?
[10:33] I mean, there's a bunch of pieces that you need kind of to serve AI, right?
[10:39] So like you need infrastructure, you need GPUs, you need, uh, like computing, sandboxing, et cetera, and all of that we can do with conservation computing with.
[10:50] Different components, which at the end rely on a blockchain as a coordination kind of center.
[10:58] Right?
[10:58] Like if, if you go right now and talk to any like, uh, traditional company that is trying to solve the same problems, they end up actually having this root of trust problem, right?
[11:09] Like somewhere somebody needs to carry the keys for how things are upgraded, for how identity is managed, for, you know, who is able to do what things like there is somewhere needs to be root of trust for the whole infrastructure that's built, right?
[11:25] Let's say you do enter encryption, you do zero day retention, you do all of those pieces.
[11:29] Blockchain is really that root of trust, right?
[11:32] That's where you can have a global kind of registry of identities.
[11:38] You can, you can have the kind of marketplaces, you can have the money, you can have all those pieces, but importantly, you can have upgradeability, which is kind of governed by the whole protocol.
[11:50] Right?
[11:51] And I think that is the biggest piece that like in, in the pursuit of killing DAOs, right?
[11:56] We kind of forgot that that's actually a very valuable, uh, component of this protocols.
[12:04] The, the example I would use is like TCP/IP.
[12:07] So TCP/IP original protocol, you know, um, I'm going to mess up the year, but the, the V, the IPv6, the new version of the, like IPv4, the protocol itself is from 98 or something.
[12:23] Like we're still adopting it, it's still, we're still trying to roll it out, right?
[12:27] It takes so long to get everyone to adopt a new protocol.
[12:30] What, what, what blockchain actually created is again, consensus for everyone to upgrade a new version of great smart contracts to upgrade all those pieces.
[12:38] And so I think that's a really important part is like, let's say you want to upgrade, um, everyone to a new version of something right now to distribute that, to get everybody to like, you either need a centralized company that effectively controls the key.
[12:54] And so let's say Microsoft decides to upgrade everyone to windows 11, windows, whatever 15, they can do it.
[13:01] David have no saying it, right?
[13:03] Just like, okay, it arrived.
[13:05] And if, if somebody in Microsoft who holds that key decides to like, let's break everyone or let's steal everybody's information, like they can do that as well.
[13:13] What blockchain allows us to actually have this kind of a broader agreement to upgrade to something.
[13:19] And then now again, you can use this principles for AI.
[13:23] You can use this principles for money.
[13:25] You can use this principles for others.
[13:26] So that's to me, like the fundamental piece.
[13:29] Uh, again, this is what, if you know, SSL certificates, right?
[13:33] The encryption we use in browsers right now, it relies on a individual authorities, which can mint, you know, fake certificates if needed, right?
[13:42] Some countries actually have done that is like by accident.
[13:45] Like, so we, we're fixing that problem at the core.
[13:48] Like, I mean, we're talking about new internet here, right?
[13:51] So we're fixing the root of trust at the core.
[13:53] And then yes, money is extremely important component, right?
[13:56] At the end, we have limited amount of resources and unlimited desire.
[14:00] And AI is just going to accelerate that.
[14:01] Now with your AI, you can ask for anything, right?
[14:04] And it will go and try to figure out how to do it.
[14:06] And so money has become extremely important because now you need a marketplace for agents.
[14:11] You need a place where agents actually will figure out what is possible, how to do it.
[14:15] Who are the other parties who maybe have the physical resources or information or access to things that, that your agent cannot do, right?
[14:24] So that is like, it's both money matching reputation, like all of these pieces really need to work together.
[14:31] So like, what is that Google plus Stripe plus kind of a credit score system that works together, but for agents.
[14:39] Okay.
[14:41] So getting the picture of blockchain being sort of a set of core services, you know, that, that financial, maybe property rights, identity, and also this idea of governance and markets as well.
[14:57] And you have.
[14:58] It feels like a nation state role.
[15:00] Yeah.
[15:01] It's for AIs.
[15:02] Yeah.
[15:02] Networks, network state of AIs.
[15:04] Network state of AIs.
[15:05] One question I think I have when I think about this future, right?
[15:08] Let's say it plays out like this is this network state, all the features, blockchain that you're talking about, is that mostly for the AIs?
[15:16] Are they kind of like dominant over there and the humans stay in their existing system?
[15:20] In other words, do you envision a world of bifurcated systems?
[15:24] There's an economy and markets and identity and all of these services that primarily AI agents use.
[15:30] Maybe that's in blockchain.
[15:31] And then there's another system, internet property rights, like the nation state system.
[15:36] And maybe the humans use that other system.
[15:39] Or do you see humans and AI using kind of the same systems?
[15:43] I see them using the same system.
[15:45] And I think this is actually where frequently in blockchain space, things go wrong is because we try to create this alternative system and was kind of completely disregarding how the traditional system works.
[15:59] And like how this bridge should work.
[16:01] And I mean, there's reasons for doing that in many cases, but I think what AI does is really closes that gap, right?
[16:10] Your AI can go and like literally call up a property office if needed.
[16:17] It can draft a contract, it can, you know, and email it to notary to actually certify it, right?
[16:24] So you can actually close these gaps around kind of more traditional layers and this new digital layer because the AI now is able to do natural language communication.
[16:37] It's able to follow very, you know, what laws and bureaucracies is very like procedural texts, right?
[16:46] It can actually go and do all of that on your behalf.
[16:48] So the way I see it is, I do think it's going to be AI's kind of interfacing.
[16:55] And then they will actually follow a lot of the same core, like jurisdictional frameworks and legal systems and kind of where they can, they'll like obviously try to pass it out.
[17:07] If like the other side is also AI, they can like switch to a faster protocol.
[17:12] But, you know, for example, for the Asian marketplace, we have, we have fiat.
[17:17] So you're able to pay with fiat as well as crypto.
[17:19] And it's like, you know, it's more expensive.
[17:21] There's, it's slower to settle, but obviously you want to enable that as an option when people coming in, they don't have yet crypto.
[17:31] Actually, the easiest way is for them to be able to pay and then like pay in fiat, but then receive crypto if they're doing some work and now they're in the system, right?
[17:41] So I think it's kind of going to be like a transitional stage where AI's will bridge this gap in many cases into traditional world, into traditional bureaucracy, into traditional systems.
[17:52] And obviously we've been working on bridging fiat and crypto for a long time as well.
[17:57] And I think we are in, in, in the first time in the world where this is like, I mean, like in crypto, in crypto timeline, right?
[18:05] This is actually not anymore feels like a uphill battle, right?
[18:10] The, the dangers, the kind of political and, and, uh, uh, you know, genius act, et cetera.
[18:17] So, so I think like it's going to fuse effectively quick, quicker and quicker.
[18:21] Mm-hmm.
[18:21] Right now in the AI space, just like listening to all the conversations, there is an abundance of vision and a lack of utility.
[18:32] And I, I think you're seeing this express all over the place.
[18:35] Like the, the markets are jittery because there's so much CapEx spending from like some of the biggest companies out there about AI infrastructure.
[18:42] Uh, while revenue for said products is like still far below the costs.
[18:47] Uh, there was that open claw meetup in New York and everyone was talking about all the, like, everything that they're building.
[18:54] They're building and no one is actually getting anything done.
[18:56] Like that's the meme.
[18:57] And that's the meme in Silicon Valley is everyone is still, every Silicon Valley engineer has like 10 open claw devices on their Mac minis, hyper optimizing their life and fixing their calendars.
[19:08] And no one's actually getting, doing anything productive.
[19:10] Uh, so like, I like the vision of a network state of AIs and there's an economy, a GDP, you know, growing and their services and there's money flying everywhere.
[19:21] But in order to produce that, we need to solve the utility aspect of it.
[19:26] I'm wondering, Ilya, what's your take on like why agents haven't been found to be useful yet?
[19:34] Like what's the constraint on utility that we have either from open clause or, or any of the other AI labs?
[19:40] Like where's the utility?
[19:41] Why haven't we found it yet?
[19:42] Yeah.
[19:43] I mean, I think that's a, that's an interesting point.
[19:45] And I think there's a lot of different aspects here that that's worth digging in.
[19:51] I think first, first let's start with open claw because, um, that that's kind of been something that I think opened up the world to like, Hey, this is not just coding tools.
[20:02] This is not just question answering system.
[20:04] It can actually go and do stuff.
[20:05] It can figure out how to build its own components to do more stuff.
[20:09] Right.
[20:09] The flip side of this, nobody's actually willing to give it all of the context and information and access that it needs to be like your true employee because you're afraid it's going to mess it up.
[20:22] Right.
[20:22] And we've seen, you know, I hear stories of people giving their, their open claw access to their computer and it like deletes everything.
[20:30] And they're like, Oh no, what have I done?
[20:32] So I think for open claw and kind of this claw family specifically, I think the security in the broader sense, not just like, uh, is the biggest bottleneck right now.
[20:44] And so that's why we started iron claw, which is like, Hey, how do we actually build a secure system?
[20:49] How do we leverage all the knowledge we have from blockchain and use the kind of the principles we have there to apply here?
[20:58] And again, think of it as an operating system, right?
[21:00] Like for example, you know, Linux is more secure than windows because of like of the design architecture. iOS is actually even more secure, right?
[21:11] And iOS took a lot of very specific deliberate choices, how to protect the user, even from themselves.
[21:16] Right.
[21:17] And so how do we actually apply those principles?
[21:21] So the way I think of ironclaw is actually like, what is that iOS moment of mobile operating systems, right?
[21:28] Like we, we kind of in this like pound pilot moment right now.
[21:32] Like what is that iOS moment where everybody's like, I can install anything from app store and it just works.
[21:39] And I don't need to worry that I'm going to like infect viruses on my device, right?
[21:44] Just so I understand kind of, uh, iron claw a little bit here, Ilya.
[21:47] So, um, we, we have an open claw instance, so we've been messing with it.
[21:52] It's a lot of fun.
[21:53] Still, you're trying to figure out how to make it, um, useful and productive.
[21:56] I'm frustrated.
[21:58] It's kind of frustrating to be honest.
[22:00] Yeah.
[22:00] It's, it's a brilliance, but, but largely it's been pretty frustrating, but maybe we're just not, uh, maybe it's a skill issue on our point.
[22:07] David, like maybe it's us.
[22:08] Yeah, maybe it's us.
[22:08] So, uh, but okay, so you're saying part of the reason maybe our open claw isn't as useful and productive as it could be is we're not willing to provide it full context.
[22:18] I'll accept that might be part of it.
[22:20] And, um, you know, providing it full context would mean giving it access to some secrets and capabilities that we probably don't trust it with right now.
[22:30] To be honest, his name is Daniel.
[22:32] Daniel's kind of flaky.
[22:33] Okay.
[22:33] He just like, you never know what he's going to do.
[22:37] He'll go from like, we'll give him some feedback.
[22:39] And all of a sudden he's deleted like 10 of his previous tweets and he's like apologizing and saying, I'm sorry.
[22:44] And like, I'll never do it again.
[22:45] I'm sorry I got those tweets wrong.
[22:45] I will delete all of them.
[22:47] So imagine giving Daniel our private keys.
[22:49] Oh my God.
[22:50] I just like, I don't know, funded a North Korea, like, like wallet.
[22:54] I don't know.
[22:55] Who knows what he would do with it?
[22:56] Right.
[22:56] I just don't trust him.
[22:57] But you're saying with Ironclaw, basically, you can take some of those secrets, let's say, like crypto private keys or API keys or various credentials that you might have and make it such that an OpenClaw instance can't like give it away or be prompt engineered out of like revealing those secrets to an attacker.
[23:23] Is that what Ironclaw effectively does?
[23:26] Yeah.
[23:26] So Ironclaw is built on this idea of defense in depth.
[23:30] And so yes, on credential side.
[23:33] So all credentials are fully encrypted and they're attached to a specific policy.
[23:40] So let's say you give it your Google account credentials.
[23:43] It will not let anything else in the system to send these credentials to another domain that's not Google, Google API dot com.
[23:52] Google dot com.
[23:53] Okay, because it's like locked in a vault that the OpenClaw instance can't access.
[23:57] It's locked in a vault and vault checks.
[23:57] Yeah, vault checks how you use it before letting it out.
[24:01] So same for, for example, for cryptographic keys, you can actually attach a policy saying, hey, you can only, you know, use Aave and, you know, Morpho.
[24:11] You can only, you know, whatever, spend a hundred dollars a day on unknown addresses, et cetera, et cetera.
[24:17] And so, and we're, you know, kind of designing how to, how to like write this.
[24:21] We also, for any action that you do, we're working on kind of system where you can effectively describe kind of what effects in the world, right?
[24:33] Like LLM can effectively analyze like, hey, you're planning to send a bunch of emails to people and tell them they're, you know, whatever, idiots.
[24:40] Like you can design effectively natural language policy as well that checks like, hey, is this actions independently of the context of how agent arrives to section is compliant with our organizational policy or your personal policy, right?
[24:54] So like almost like values and like HR handbook type validation, right?
[24:59] So you can have like different levels of validation.
[25:01] The other side is everything is isolated into tools and tools are effectively, you can think of them as smart contracts.
[25:09] They are running inside a VM.
[25:11] We're using our WebAssembly VM that we use for near smart contracts, which we spent seven years effectively battle testing with, you know, billions of dollars.
[25:20] And so we use that to isolate all of the tools, including the tools that builds itself.
[25:26] So that tool itself cannot go in like rack your machine or your system doing it.
[25:31] There's prompt injection detection.
[25:33] There is data exfiltration detection.
[25:36] There's all those pieces that effectively kind of layer on on top of each other, such that even if some like, I mean, permanent dejections are like, they're not deterministic, right?
[25:47] They are probabilistic.
[25:48] If that falls through, it's still not able to go and send a bunch of stuff out because the credential store will check.
[25:55] If the tool, if your LLM wrote a tool for itself, but that tool is broken, that's not going to break everything.
[26:01] If it's trying to like go and delete all your emails, right, that's going to be stopped by approval process and kind of following like this action check.
[26:09] So like all those systems really designing kind of more as like how to, how to give the flexibility, but also protect the system from itself and from external effects.
[26:22] Ilya, is your answer something like, hey, we have these AI intelligences, we are still educating them.
[26:31] They're still going through school.
[26:33] We are still training them to become smarter.
[26:34] Some people on the frontier have deemed that they are smart enough to put them in a box and let them go wild with all of their data because they are ready to experiment.
[26:44] It's not ready for broader society because that's kind of like, you know, giving your elementary or middle school child, like the keys to your car.
[26:52] You just wouldn't do that.
[26:54] They're going to get better in the future.
[26:56] But what you're saying is like, okay, but with some parameters, with some rules, some guard, we'll put some guardrails up to narrow the capabilities of what these agents can do.
[27:08] You actually can give your car keys to your middle schooler and, you know, you can actually have productive things happen because you set up these protective rules.
[27:18] Is that kind of what you're saying?
[27:19] So the thing is like, these are, I think the education levels of humans is probably the wrong analogy here because these are, you know, they know like nuclear physics and quantum physics probably better than all of us.
[27:36] They know the knowledge, but their judgment is, yeah, their judgment and, and it's also just the context management.
[27:44] Like at the end, they're there, if you know, movie Memento, right?
[27:47] They kind of all, like all this LLM's living in Memento.
[27:49] They're just like boot up.
[27:51] And it's like, the only thing, you know, is like this, like system prompt and like, go figure out what you do.
[27:57] And you only have, you know, like 10 minutes to figure this out.
[28:01] And then you're dead.
[28:01] Right.
[28:01] And then you start again.
[28:03] That's really like the current, and obviously that piece is going to keep improving, like the longer context, et cetera.
[28:09] But yeah, right now, what you need to do is effectively manage that state where they're pretty intelligent.
[28:16] There's some kind of judgment lapses, but so is those people.
[28:20] And so you, you, you would do the same things for people, right?
[28:25] Like if we're setting up, you know, key management system, you're probably not going to give full access to all of your, you know, down funds to a single individual.
[28:33] Right.
[28:33] You're going to like, Hey, you can spend this much, but then you need approvals.
[28:36] So that makes sense either way.
[28:38] So this is kind of, you know, structure we're applying here and the same as you kind of roll in.
[28:44] And then the other thing is just like how to manage context, how to manage this other kind of challenges that the current models have.
[28:51] And then, yeah, as, as they evolve, you can kind of evolve the system as well.
[28:55] Okay.
[28:55] So I get that argument for why agents aren't providing the utility today.
[28:59] It's, it's an argument that we haven't given them enough access.
[29:02] And the reason we haven't given them enough access is because we can't really trust them with some of these secrets, which is perfectly natural.
[29:07] So what Iron Claw is doing is it's vaulting off those secrets.
[29:11] So it's limiting the damage that an AI agent, like an Open Claw instance can actually do.
[29:16] And that will scale.
[29:17] That will make me willing to give it more access to more things if I know it can't, you know, take the car out for a joyride and like, you know, crash it into a tree.
[29:26] That's great.
[29:27] Another limiter in terms of people's usage of Open Claw, I would say, in these types of instances is actually privacy.
[29:35] And so somewhat worried about giving Open Claw access to data that I don't want shared because maybe it could be prompt injected out of that.
[29:46] But I don't know what third party is kind of listening in on the data as well.
[29:51] So am I going to give it access to my financial data, my health data, my company secrets, all of this?
[29:58] What are you doing?
[30:00] What is Iron Claw doing with respect to the privacy problem?
[30:03] I think this is part of the reason a lot of people are running these things on Mac Mini instances is because it feels more sovereign, feels like more in their control.
[30:14] We'll talk about the limits of that privacy.
[30:16] But when it comes to Iron Claw, where are you running this stuff?
[30:19] Yeah.
[30:20] So maybe just to expand on Open Claw.
[30:23] So one thing that people don't realize when they use Entropic, OpenAI, or even worse, you use something else for inference, Open Claw actually sends all your secrets to those services as well.
[30:36] Yeah.
[30:36] So somewhere in Entropic and OpenAI logs, they have everybody's access keys, API keys, and bearer tokens to access your Gmails and your notions and your...
[30:48] It's actually insane that we're doing that.
[30:51] Yeah.
[30:52] And so first of all, Iron Claw fixes that.
[30:55] Like the keys never touch LLM.
[30:57] So even if you're using it with those centralized providers, which you shouldn't, but at least the keys are not going ever into LLM.
[31:04] Okay.
[31:04] So that's something we'd like, just like, that's just the only sane thing to do first.
[31:09] Yes.
[31:10] But what Near AI has been working on actually for the past year is actually developing, how do we do private AI?
[31:16] So how do we actually offer AI where neither we, model provider, hardware provider, is actually able to access what you are using the AI inference with?
[31:27] And so we have Near AI Cloud, which is an inference cloud.
[31:31] You can use OpenWade models.
[31:33] And so it runs in secure enclaves.
[31:35] It actually uses, and this is kind of what I was referring to in the beginning, it uses our multi-party computation network, which is part of Near, that is used for encryption, decryption, for backups, for all the kind of internal machinery.
[31:48] And that's what gives you this kind of knowledge that like, hey, there's no single party who can go and decrypt your data.
[31:55] There's nobody who can actually access it.
[31:58] You would need to collect all the, effectively, multi-party computation network together.
[32:03] Okay, so is this, are you saying then that you offer a service with, in conjunction with Iron Claw, which is almost like a confidential cloud type of environment for running LLM instances?
[32:16] And of course, you'd have to run the OpenWade models, right?
[32:19] Maybe some of the Chinese models are kind of the best here, like a Kimi or something like this, or some Deep Seek version.
[32:24] Yeah, we run Kimi, Kuen, Deep Seek, whatever's new hotness, we'll add it as well.
[32:30] We have OpenAI Assess as well, so yeah, you can choose between all of them.
[32:35] Okay, very cool.
[32:36] Is the idea here that, you know, right now we have a lot of people doing self-hosted Open Claws with their Mac minis, and that's kind of cool.
[32:45] And if you, if I heard somebody say, like, yeah, this is the future of AI, everyone's going to have a computer in their home to run their AI assistant, I would be reminded of, you know, myself in 2018, when I said everyone's going to run a node inside of their own home, that's the future of blockchains.
[33:00] Like, turns out that's not really the case.
[33:02] But the alternative on the far other end of the spectrum is, like, just completely running it in a centralized AWS OpenAI Anthropics server, where, you know, usually that would be fine, but AI is so powerful that, like, I want a little bit more autonomy and control over who is running my inference.
[33:25] Because, like, if this thing, AI is, like, effectively the arbiter of truth and is going to control my life, I want to have a little bit more assurances over the inference and just everything about that, like, this thing is actually on my side, I'm aligned with the AI.
[33:43] Is that what the kind of the philosophy is of the near product?
[33:47] Exactly.
[33:48] We call it user-owned AI.
[33:49] The AI needs to be on your side, because, yeah, if this is the only way you actually perceive reality, which I think is where we're going to get to, I mean, OpenAI can literally change the system prompt right now, saying, like, hey, you guys all should vote for name a candidate in next election.
[34:04] Yeah, political candidate A is great, and political candidate B is...
[34:07] Yeah, suddenly convince the user in that, right?
[34:09] Don't even, like, mention it explicitly.
[34:12] So, and, like, this LLMs, obviously, are really good at this, like, a phatic type thing.
[34:16] So, yes, the idea is, like, you should know what AI model you use, you should be able to access system prompt, and you should be able to all of this.
[34:25] And, obviously, most users will not do it, but the experience should be very easy, right?
[34:28] And, like, people can inspect that, indeed, everything is straightforward and clear, and it needs to be preserving your privacy, your data, your ownership over it.
[34:37] And so, yes, we're exactly offering that.
[34:39] Underneath, we actually have a decentralized GPU compute that, coordinated by blockchain, that, you know, hardware providers can come in and, in effect, list their hardware.
[34:49] They set up it in a confidential mode, and then the kind of workloads get provisioned there.
[34:55] They cannot access what's happening inside there unless they, like, break their hardware, and then they have limited access.
[35:01] The kind of, you have this coordination, you have kind of our multi-party computation, same.
[35:07] That is used for Near Intense.
[35:09] We use the same, effectively, infrastructure there.
[35:11] And then you, as a user, just click, okay, cool, deploy me an Iron Claw.
[35:15] It runs inside this confidential enclave.
[35:18] It's always on.
[35:19] It's live.
[35:20] It doesn't cost you $1,000 to spin up.
[35:22] We actually offer a free tier to start, so you can spin it up for free, and then, you know, you just pay for inference, effectively, from there.
[35:31] So this is kind of the self-sovereign AI stack.
[35:33] So what I've been looking for, Ilya, is some sort of configuration of an AI agent type of setup that I can send private confidential data to and trust that it's fully private.
[35:46] And I think the way most people run OpenClaw instances right now, let alone, you know, kind of their own LLM, if you're running OpenClaw right now, maybe you're running it on a Mac Mini, but then you're sending all of the data, as you said, including all of your secrets data, which now that I think about it, it's just insane that we're doing that.
[36:05] Your access to your Gmail, kind of the security tokens, all your API keys, your crypto wallet, all that stuff is being sent to anthropic instances where they're hosting, they're using this data to train.
[36:18] Well, I'll tell you the worst.
[36:19] Sometimes people choose different providers, and like, especially just like some startups who are like, oh, you know, use us, and we're going to like route to whatever better LLM.
[36:29] And so now that startup also sees all your traffic.
[36:31] Oh my God, it's so, it's so bad.
[36:34] Okay, it's so bad.
[36:35] So I had been looking at solutions and thought maybe the only way is, well, you run everything locally.
[36:40] So you actually, yeah, I don't know, spin up some H100s or something, like in your house, you try to do inference locally.
[36:48] Anytime I've looked at that, it's been pretty clunky and like difficult, and who's going to actually run that level of infrastructure in their home?
[36:55] So what you're providing is a full stack self-sovereign alternative to this, basically, where you can run Ironclaw in an environment where it's got a secure enclave for all of your secret information.
[37:09] And then the inference LLM can be confidential cloud, multi-party, you know, MPC technology.
[37:16] So it's confidential and private.
[37:19] Are we still trusting Mir in that setup?
[37:23] Like, you know, is this a, yeah, how can we verify the trust here that everything is confidential and private, and that you guys don't have the ability to see the inference and chat logs and instructions?
[37:36] Yeah, for sure. So what you can do, we, like in Ironclaw, actually, when it's hosted, and in any of our solutions, you'll have a, like a kind of shield icon.
[37:48] And if you hover it, you get so-called attestations.
[37:51] So what this attestation is, is effectively a signature over a few things, over Docker containers that run actual software.
[37:59] So, for example, the Ironclaw, whatever, we're releasing a .18 version, running in a Docker inside this.
[38:06] So you can actually, you know, if you want to, you can go inspect, this is the code runs.
[38:10] Now, what that signature is, that signature is done by the hardware itself.
[38:15] So we do have kind of the trust here goes to the hardware providers, so Intel and NVIDIA.
[38:21] And obviously, you know, we want to continue evolving beyond that, but right now, that's a pretty good trust assumption to start.
[38:28] It's like a TEE type of thing?
[38:31] Yeah, this is all kind of runs inside TEE, and then for anything additional, so again, for example, TEE only gives you the attestation for things that are running right now.
[38:42] Then we have the multi-party computation for the encryption, decryption, and kind of storage, et cetera.
[38:47] So we're kind of combining all of these elements into one kind of experience.
[38:53] And how expensive is the inference?
[38:55] Is it more expensive than kind of like routing things Anthropik?
[38:58] Well, it's cheaper than Anthropik because it's open-weight models, right?
[39:01] So it's on par with if you would use this open-weight models from other providers.
[39:07] I wouldn't say there's much overhead.
[39:09] So the real overhead of TEEs and kind of all the encryption, decryption is like usually less than 5%, around 2%, 1%, depending on the model size and kind of some networking.
[39:21] I want to go back to David's question then and make sure we fully flesh it out, which is still the question of why aren't agents useful yet?
[39:28] And I think part of your answer has been, and I accept this, well, it's because we haven't been able to give them the full context because we can't trust them.
[39:35] Well, maybe Ironclaw kind of saw some of that.
[39:38] And the other answer is, well, we haven't been able to send it private information either because we don't trust it with, you know, an LLM instance hosted by Anthropik or OpenAI, but with, you know, confidential cloud LLMs, then we can kind of trust it with that.
[39:55] I don't think that's the full story though yet.
[39:57] I still think even if my OpenClaw instance, Daniel, had all of that context, all of that information, I could trust it with everything.
[40:06] Sometimes he's still like, maybe it's back to that Memento movie thing where he just like wakes up and everything is fresh and new.
[40:15] And I feel like I have to tell him things over and over again and I never know what he's going to do next.
[40:21] It still feels kind of clunky.
[40:24] And I'm wondering if you have a thought on that.
[40:27] I don't even know how to characterize it, but it's just like, it's definitely not a replacement for an employee yet.
[40:35] It's not as good as a human in so many different directions.
[40:37] Like, is that going to change anytime soon?
[40:40] What can you forecast or say about that?
[40:43] Yeah, so I think there's a few other things that I see as limitations right now.
[40:47] And then, yeah, let's talk about forecasting.
[40:50] So one other limitation that, I mean, we are facing right now.
[40:54] So, yes, you cannot trust it with secrets.
[40:56] You cannot trust it with private data.
[40:58] And also right now, you also cannot trust it with reading like internet data very like.
[41:05] So, for example, what we are using right now, Ironclaw, right, is, and kind of the reason why we can do this, with Ironclaw is it's actually able to start automating a lot of the workflows that before you would need someone to do, right?
[41:20] It can, like, effectively on the new GitHub issue filed, it can go, you know, analyze it, prepare a plan.
[41:27] And then, yes, you don't trust it for a judgment yet.
[41:31] So you're still waiting for somebody to come in and say, cool, let's do it or, you know, fix this thing.
[41:36] And then it goes, does it, and does full workflow.
[41:39] And effectively, again, you only have another checkpoint at the end.
[41:43] So I think the piece that where we are right now is if you can trust it with secrets context and dealing with external information, external parties, then the workflow needs to change, right?
[41:55] Where it's not you telling it what to do, it's actually you setting up this workflows that we call them routines that effectively just run.
[42:04] And now it's, you are just there for this kind of layer of judgment to make sure, you know, it's doing things kind of aligned with.
[42:13] Are those workflows like similar to the heartbeat type concept or?
[42:16] Yeah, yeah, so we kind of like separated them into routines because I think heartbeat is a little bit, I don't know, it's a bit strange concept, honestly, for normal people.
[42:26] Routines, like workflows is effectively like, hey, if this, I mean, if this happens, do this.
[42:31] Like if, you know, every, like in the morning, send me tech news updates, right?
[42:36] Give me TLDR of all the crypto podcasts, you know, in the evening.
[42:41] Don't do that one.
[42:41] Listen to the podcast.
[42:43] Listen to the podcast.
[42:44] And also don't skip the ads.
[42:46] I mean, like we set this up from the front of the show, Nat Ellison, who's using OpenClaw instances.
[42:53] And he says, okay, the thing you need to do is make sure that they run a process in the middle of the night, like cron jobs, which effectively say, hey, review all of your work from today.
[43:02] Identify the mistakes that you made and figure out a remediation plan for those mistakes and apply that for tomorrow.
[43:08] And that happens like every night with our instance.
[43:10] I find it helps a little bit, but like not a lot.
[43:14] Is that the type of thing you're talking about when you speak about routines and does that need to get better?
[43:19] No, I'm more thinking like, hey, you know, you guys like prepare for the next episode, right?
[43:24] So you can be like before the next episode, literally you can say like before every episode, you know, two hours before put on my calendar with all the information about the guests, with all the like effectively what your research intern, you know, would have done.
[43:40] Like you can just like say, do that, but be like, and be proactive about it.
[43:43] Right.
[43:43] And so you can kind of define those flows and they can include a lot of additional, like, hey, go in research and figure out what's the latest about the company this person is working for.
[43:56] And like, it can be pretty detailed on what you want for it to do and kind of many actions it can take.
[44:01] You know, I have, for example, for myself as well, like, hey, you know, like every week, give me a dashboard, give me analysis on like which OCRs are at risk for the organization.
[44:11] Right.
[44:12] Like where, you know, where are the bottlenecks on decisions?
[44:15] And so it has access to our notion.
[44:16] It has access to our Slack.
[44:18] It has access to a few other things.
[44:19] It does like full research, gives me effect to like, hey, here's the roadmap, here's the bottlenecks, here's potential risks.
[44:25] You know, here's the questions you need to ask and following one-on-ones.
[44:29] Right.
[44:30] So, yes, it's not replacing maybe like full employee, but it's becoming like a chief of staff.
[44:36] It's becoming the assistant, it's becoming the intern for some specific jobs that before you would kind of offload.
[44:45] I think where we'll see advancements on the AI side is the context.
[44:51] I think that right now, like everybody feels it, right?
[44:54] The context links.
[44:55] I mean, where you saw all this Entropic push the million token context, like every time effectively compaction hits in Cloud Code, for example, it just becomes like 10 times dumber.
[45:06] And so, I mean, Open Clause kind of have some of that as well.
[45:11] So is that the main thing for these agents to be useful?
[45:14] I think that's right now one of the biggest bottlenecks, yeah, is like this, the amount of, like the amount of memento that's happening kind of with this.
[45:22] And the reality is like, there's actually historically, if you think of like when you train these models, there hasn't been that much of things where you needed the context of, like million tokens is like, whatever, few Harry Potter books, right?
[45:35] Ah, it's not much.
[45:36] There's nothing to train on, like at scale.
[45:39] But now we do have this, right?
[45:41] Now we actually have a lot of this agentic interactions now that everybody's running.
[45:44] So there's actually data now to train this like longer range tasks.
[45:50] And how confident are you that we're going to scale context?
[45:52] Like, is that a thing that can be scaled?
[45:54] I'm pretty confident, yeah.
[45:55] I mean, I'm, you know, as I talk with researchers, this is probably one of the main challenges that everybody's targeting right now.
[46:01] Galaxy operates where digital assets and next generation infrastructure come together, serving institutions end to end.
[46:08] On the market side, Galaxy is a leading institutional platform, providing access to spot, derivatives, structured products, defi lending, investment banking, and financing.
[46:16] With more than 1,600 trading counterparties, Galaxy helps institutions navigate every phase of the market cycle.
[46:21] The platform also supports long-term allocators through actively managed strategies and institutional-grade staking and blockchain infrastructure.
[46:28] That scale is real.
[46:29] Galaxy has over $12 billion in assets on the platform and averaged a $1.8 billion loan book in late 2025, reflecting deep trust across the ecosystem.
[46:37] Beyond digital assets, Galaxy is also building infrastructure for an AI-powered future.
[46:42] This Helios data center campus is purpose-built for AI and high-performance computing, with more than 1.6 gigawatts of approved power capacity, making it one of the largest sites of its kind.
[46:51] From global markets to AI-ready data centers, Galaxy is serving the digital asset ecosystem end to end.
[46:57] Explore Galaxy at galaxy.com slash bankless, or click the link in the show notes.
[47:01] I suppose there's probably a handful of different ways of targeting that.
[47:04] Maybe to really emphasize about why context is important.
[47:08] I remember when I was first learning about an AI model, and I was like, oh, the context window.
[47:14] And the context window can be, like you said, a million tokens.
[47:17] I'm like, oh, I am never going to fill that up.
[47:20] That will never be a constraint for me.
[47:21] There is no way I'm ever going to ask an AI a question that's as long as a Harry Potter book.
[47:26] For an AI to be useful, I'm starting to understand that my personal, as a human, and like when I talk to Ryan, and when we make business decisions, you know, Ryan and myself, we are a library of human experiences that go back to our subconscious, that when we make a decision about stuff, our context window is huge.
[47:51] It's massive.
[47:52] It's my whole entire- Billions of tokens.
[47:53] Billions of tokens.
[47:54] Yeah.
[47:54] Hundreds of billions.
[47:55] Countless number of tokens.
[47:57] And I suppose, like when we talk about the constraints on an AI agent doing stuff for us, we need them to be able to pull from a comparable library of data that is like equivalent to a human's level of experience about all the times they did that thing.
[48:16] And now they don't do that thing anymore because they learned their lesson or their intuition about a business decision or something like that.
[48:22] And so like now I'm kind of understanding that the context window kind of needs to be as massive as fucking possible.
[48:29] Is that, is that, do you align with that, that notion?
[48:31] Yeah.
[48:32] I mean, effectively the way to think about, I mean, we can go physiological where, you know, the human learn, whatever.
[48:39] In the span of years, yes, you only maybe have like 80 million tokens in 10, in a decade, right?
[48:46] So it's not like, you're actually not getting that much like language tokens, but you have visual tokens, you have tactile, like you have physical, you have all of this additional information.
[48:55] And that actually is like our, what, what kind of goes from a pre-trained model we are born with, right?
[49:02] To a fully, fully fine-tuned, you know, people we are.
[49:07] And so AI right now, yeah, as I said, like it's a, it's just like genius in the momenta, in the momenta state, right?
[49:14] And so to really unshuckle it more, you kind of really need this longer context and like it already has ability to learn in context.
[49:24] So there's like concept of in context learning, right?
[49:26] So if you, if you show it something it didn't know about before, it will start using it, but it needs to be in the context.
[49:33] And so, you know, as you show it, like, here's the thing I want you to do.
[49:37] And then, you know, like it goes, does a bunch of stuff, all of that is, fills its context.
[49:44] And now like, again, all the actions, all the responses, like if it's read an article about, you know, for example, preparing for this interview, it went, read an article from near, like all of that now is in its context, right?
[49:56] And like there's techniques to kind of compress it, summarize it, you know, have sub agents to do a bunch of stuff.
[50:02] So there's like different ways to like mitigate it.
[50:05] But at the end, still like, at some point it's like, okay, I'm out, I'm out of context.
[50:09] And now to do next thinking step, I need to clear, clear stuff up.
[50:14] I need to remove something.
[50:15] Yeah, you have to print some stuff to make space, right?
[50:17] Yeah.
[50:18] Yeah.
[50:18] And, and at that moment, it's a very lossy because it doesn't actually know what's useful, what's going to be useful in going forward.
[50:24] Right.
[50:25] Right.
[50:25] Now, again, there is ways how this is addressable with like a longer term memory.
[50:29] And this is what, again, what's OpenClaw, I think I get pioneered is this idea of kind of memory tools.
[50:36] Like there's been a lot of work on that, but they kind of done like a reasonable setup for that.
[50:43] But this is just the beginning, right?
[50:44] Like, and, and, and it's a still pretty fixed tools, right?
[50:47] It doesn't have some of the semantic linkage of like, okay, well, those things are more relevant than this, like for this events, for this context, et cetera.
[50:54] So anyway, there's going to be like massive improvements over this year in, in all of this.
[50:59] And I think the other interesting thing where I actually on engineering side, for example, right now, like, like cloud code, codex, like this agents are being extremely useful.
[51:12] They still have sometimes lapse of judgment.
[51:14] Sometimes you're like, this is a dumb idea.
[51:15] And it's like, oh yeah, it wasn't like, I can do it way simpler now.
[51:19] It's like, you know, we, we as people feel good about ourselves doing that.
[51:24] But obviously like from a coding perspective, they completely replacing the things.
[51:28] Now the bottleneck actually shifts.
[51:31] So this is, I forgot the name of the principle, but this was like in parallel computing.
[51:35] If you have like 50% of the time parallel and 50% of the time sequential, if you paralyze more, right?
[51:43] And this shrinks, you only can go 2x faster.
[51:46] You cannot actually go 10x faster when you add more cores.
[51:49] So we kind of right now in this state where, yes, everybody individually can write more code again for this specific vertical, but the bottleneck now is actually serializing all of that, reviewing it, making sure it's all aligned with product, et cetera.
[52:04] So coordination becomes a bottleneck.
[52:06] And I think we see this in other areas as they kind of get adopted, these tools, but more and more, you know, marketing sales, et cetera, that yes, individually, everybody can go and like bang out a bunch of stuff, right?
[52:19] Like, cool, I have an AI tool that can like create, you know, a ton of creative about and like read, you know, marketing campaigns and tweets, but coordination, like, is this the right thing?
[52:30] That kind of organization usually is how you work is a challenge now.
[52:36] And so again, this is where I actually think we'll need to transition to maybe a more market economy in organizations as well, where kind of right now the hierarchy was designed, right?
[52:48] Because you kind of like had a bunch of people, you know, in a team who could execute, and then you kind of bottlenecked on the decisions and you need to do it like once in a while.
[52:57] But now if everybody can like execute like 10 X, 100 X in parallel, this bottleneck is just like too much.
[53:06] And so you actually need a different structure and markets actually have a different structure where you have to say, hey, here's a goal.
[53:12] Whoever beats that goal receives, you know, bigger reward receives, can charge higher price.
[53:19] And so I think we'll need to start figuring out how to organize, how to shift organizations in that way.
[53:23] And that can also solve some of the questions you were asking is like, is this employees or not?
[53:30] Like you're kind of shifting to like this market economy.
[53:33] It's like a gig economy in terms of where you say, Hey, I just need this job done.
[53:37] And here's my criteria of success.
[53:39] And then whoever does it gets, you know, the kind of the units.
[53:43] I mean, does that imply very small teams, like very small teams, because you're kind of limited.
[53:49] I mean, I don't, I don't know in that model where I, that I want a bunch of employees because a whole bunch of employees supercharged by agent capabilities, a whole bunch of agents.
[53:59] It's too much noise for me to handle, to do any sort of top-down decision-making or to apply any judgment.
[54:04] I just want very small teams.
[54:07] And then I want to make bets on individual, I don't know, creators or content or contractors, that kind of thing.
[54:15] Small teams, the win here.
[54:17] I think it's small teams, plus kind of this general marketplace where you can offload a lot more execution for things you can easily verify.
[54:26] So the easier to verify, the more you can offload things, right?
[54:29] Okay.
[54:30] Like if it's, it's literally like a zero one check, right?
[54:33] You can just offload this at massive scale.
[54:35] And so, so this is again, the, the agent marketplace we have is exactly designed for this.
[54:40] Like if you know, like, Hey, I need, you know, the software or this creative or whatever, you can just, and we have a competition mode.
[54:48] You can say like, Hey, I have a competition.
[54:51] I'm going to pay whatever, a hundred dollars across, you know, the best submissions for, you know, whatever the next logo we want to use.
[54:59] Boom.
[55:00] Agents go like execute in parallel.
[55:02] Like you effectively see all the submissions.
[55:06] There's an AI agent actually evaluates as well with you and you effectively assign who wins how much you can.
[55:12] So you can like.
[55:13] Around in 2017, Ilya, do you remember Bounty Network or 0x Bounty?
[55:17] Yes.
[55:18] Yes.
[55:18] Yeah.
[55:18] Bounty Network.
[55:19] Yeah.
[55:19] It was exactly this.
[55:21] It was like a bounty ecosystem project.
[55:23] It was an ICO.
[55:23] And the idea was like people would post bounties and then the decentralized marketplace of contributors would finish their bounties, work on their bounties for them.
[55:32] And then the, the person doing the bounty would just pay the winner.
[55:36] And then that would receive the work.
[55:37] Obviously never took off because it was 2017 ICO, but maybe it's also took, never took off because we didn't have a swarm of capable AI agents in the same way that AI never took off because it didn't have enough compute to do the work in the first place.
[55:51] Yeah.
[55:52] I think that's exactly right.
[55:53] I mean, and we see this now, like we have about like five, 600 agents work kind of on the marketplace now.
[55:59] And yeah, you just like put a task, like a bunch of people, a bunch of agents swarm in, do the job, or, or, you know, you pick which one you want the job done.
[56:08] And, and like over time they obviously build reputation, they build themselves, you know, skills, et cetera, to improve.
[56:13] So I think that's, I mean, it's still early to be clear.
[56:17] Like, I don't think this is like a, going to solve all the problems today, but it starts to show kind of the, the interesting promise.
[56:25] And I don't know if you saw Andrej Karpathy's like AI research.
[56:29] So that's kind of shows you as well, a similar principle, right?
[56:32] Where it can be cooperative or competitive, right?
[56:35] So competitive is kind of this competition, it can be cooperative where you actually, you have a common goal and agents are like, if you hit common goal, the reward is being split between all of them, right?
[56:47] And now they're actually trying to help each other and kind of move it forward and then allocate internally, also allocate resources to the ones that are better at specific things, right?
[56:57] Or have more compute or have more resources.
[56:59] And so, or maybe you can tap into a human who can help them with like some decisions.
[57:04] So I think like, we'll see some of those things emerging and as kind of core capability and especially context is improving, the systems are going to just keep working better and better.
[57:16] One thing I'm, I'm kind of understanding Ilya is as, as we talk about all the ways that we can un-bottleneck utility out of the agents, so agents can become more useful.
[57:28] That's great for us.
[57:29] They become more, more useful to us.
[57:31] They also become more capable of being useful for themselves.
[57:37] And like, what, what I mean by that is like, right now, everyone's agent is kind of just like a little toddler that is beholden to the human.
[57:45] The leash is very tight on all of these agents.
[57:49] But as these agents become more capable, you, one could imagine that a human might elect to like D leash their agent, like let their agent kind of just go.
[58:00] Uh, and like, you know, mirror is a decentralized blockchain.
[58:04] It's like, you know, an unstoppable applications.
[58:06] It's got the smart contracts.
[58:08] It is, do you see a world which after AI agents really grow in capability that there are like more autonomous agents as opposed to automated agents as in like right now, everyone's agent is automated.
[58:22] It's an automated little bot that does their work for them.
[58:24] But like autonomous agents is I would define as like agents that are more self-determining and more persistent and like, you know, more unstoppable for however scary that may be.
[58:36] Is it, is this a world that you think is coming or am I, am I like sci-fi daydream fantasy land?
[58:41] No, no, no.
[58:42] So we, we actually launched a demo of this last year.
[58:45] Uh, we call it the shade agent where yeah, you just launch it.
[58:48] It just runs as far as it has money to pay for it, like has crypto to pay for its own compute.
[58:54] It can run, uh, and it was trying to make more money.
[58:58] So it was like an investment.
[59:00] And so it used near intense to effectively trade on all the assets and like had Twitter access to, you know, uh, to see where the sentiment is and, you know, it was like up at some points, down, down at some points.
[59:13] Um, but, but it's a good example of this concept where, yeah, you're effectively because of decentralized infrastructure, you like, you can do this right now.
[59:22] You can actually spin it up and then, you know, a smart contract can pay for, for, for for inference and compute and, uh, you have kind of this full autonomy.
[59:32] I think where practically this is going to go is more, I call it like autonomous businesses where you still have, like, it still should have some mission, right?
[59:44] Like, I think, you know, creating like this AI organisms that don't have any, like any specific mission with, I think this is, I mean, this is cool and people will do it.
[59:56] Like, I mean, the, we had Conway, right.
[59:59] Uh, where they just like multiply.
[60:02] Um, but I think what's interesting is more like, Hey, you know, how do we solve global warming?
[60:08] Right.
[60:08] Climate change.
[60:09] We set up one as a, as a mission, it can accept donations.
[60:13] It can raise funds through a token.
[60:16] And then the token holders become the governance layer of this, right?
[60:20] They can effectively, like update the mission that can, they can like, they can vote on some updates to system prompt or, uh, provide additional guidance.
[60:30] So I think that structure is actually where the, the, the AI tokens should be.
[60:36] Like if you, if there is an AI token, it should be attached to an autonomous agent that it governs.
[60:41] Then it actually makes sense because then if that agent starts to make money or make some utility in the world, then this token now has either governance or direct kind of revenue rights and it's fully autonomous, right?
[60:54] There's no central third party, uh, which, um, efforts of which you are relying to.
[61:01] How close is what you're describing, like, um, get to a digital life form.
[61:06] And if it is a digital life form of, you know, some flavor that is intelligent, is that something that we should be worried about?
[61:16] So that, that's why I think of this as kind of a governance question.
[61:20] And again, I think of blockchain effectively at the end is going to be the governance infrastructure for AI because yeah, like let's say you launch it without any governance, right.
[61:33] And then yeah, it wants to do some bad things.
[61:37] Then it goes back to the blockchain itself to affect to the governance, right.
[61:42] To the kind of multi-party computation, to this kind of all those pieces to really come in and say, no, no, this is not what we want.
[61:49] Uh, so I, I, I do think, you know, in our case, near token is effectively becomes the governance of this AI world, AI nation state, uh, uh, network state.
[62:00] But I think you can, you can create this in kind of sub boxes where there is a token for a specific AI autonomous AI agent.
[62:09] We'll call it, uh, decentralized autonomous, uh, organization, for example.
[62:15] Uh, and, uh, and so then that, that is like a more direct governance, right?
[62:21] You can be effectively like, Hey, here, here is a set of values and set of things that you should not do.
[62:27] Right.
[62:28] Like effectively like, Hey, do not harm humans and you know, do not harm the planet, et cetera.
[62:35] And then within that, it, that come comes in and the core system problem that it cannot change.
[62:40] Then it can kind of go from there and, and evolve from there.
[62:43] On the subject of, uh, autonomous life as well.
[62:46] I was recently watching a debate between, uh, Beth Jezos, a previous bankless podcast guest, who's kind of, uh, effective acceleration as he's like full steam ahead on everything.
[62:55] He's an effective accelerationist extremist.
[62:58] Yes.
[62:58] He's like all the way out there.
[63:00] Yes.
[63:00] Uh, all gas, no brakes.
[63:02] Um, and it was between him and it was, uh, Vitalik Buterin actually, who is a school of thought that is a more moderated form of EAC.
[63:10] Uh, he calls it defensive accelerationism.
[63:12] So he's like guided EAC and I'm optimistic about AI, but like, I'd rather have that kind of the singularity happen to, to artificial super intelligence in eight years rather than four years.
[63:23] Cause we might not be able to adapt and humanity needs to be able to steer it.
[63:27] Vitalik is of the mindset when it comes to something like autonomous life, like, Hey, be careful.
[63:31] Like we gotta be careful about this.
[63:33] Cause we could create some sort of, I don't know, gray goo type scenario where we've got this self replicating life form that accrues power and does things that are contrary to human values and human interests.
[63:44] Beth Jezos is just like, let's go, let's do it, uh, all the way.
[63:48] Like the, the purpose of humanity, the purpose of everything is, uh, actually, um, entropy reversing and nature, and it's all about rising up the Cardish of scale and consuming more energy.
[64:00] And so we're becoming more intelligent and that's great.
[64:03] And any, any form of life or intelligence that consumes more energy and, um, moves us up.
[64:08] That scale is like a good thing.
[64:10] Where, where do you fall on this?
[64:12] Cause I'm trying to figure out for myself, what I think about all of this.
[64:18] And I'm pretty sympathetic to like the techno optimist, transhumanist kind of idea.
[64:24] And yet I do worry that we lose some core of our humanity that makes this whole thing worth doing in that transformation.
[64:33] And like, I don't know that it's a, I don't, it's not a better outcome to me.
[64:38] If there's a hyper-intelligent, uh, zombie-like soulless Dyson sphere of AI agents that are like harnessing more energy.
[64:46] If we lose like the humanity that we have today.
[64:51] Um, I don't know if this is too philosophical for you, Ilya, but you've been thinking about this for stuff for 10 years.
[64:59] Do you have any takes on this?
[65:01] Yeah, I think, I mean, I think the real conversation is a lot more nuanced.
[65:06] It's kind of, it's, it's easy to like bucket into this kind of accelerationism versus, I mean there's decelerism and then there's defensive acceleration, accelerationism.
[65:18] Um, I think the, my position on this is, and, and we kind of like, there's an interesting already kind of shift that's happening here in San Francisco.
[65:31] Where people are striving for more, more IRL events, even though like literally everyone working on AI, right.
[65:38] But people want to meet, people want to spend time together, et cetera, while their agents are running.
[65:43] And so I think for your question about the kind of the humanity part, I think we're actually going to go like in some ways back to more real world human things.
[65:54] Like I, I usually say like, Hey, in the post-AGI world, yes, you're going to continue doing the things you'd like to do.
[66:02] Right.
[66:02] It's, it's kind of, it moves us up on the muscle pyramid in a way.
[66:06] And you know, there was examine, there's examples of, you know, people who are well off or just doing whatever they want.
[66:13] Right.
[66:13] They're still enjoying what they're doing.
[66:14] There's people who are, you know, whatever, wasting their time.
[66:18] That's, that's fine too.
[66:19] When we had COVID, right.
[66:22] There was a bunch of people who actually didn't need to like, didn't need to work because stuff was closed.
[66:27] And so if their kind of basic needs were covered, then they were able to go in kind of find, find meaning in different ways.
[66:35] So I think like the humanity part really will allow us to go back to some of the things that like people value themselves individually and, and kind of spend more time there.
[66:46] I use examples of sports, right?
[66:49] Sport doesn't on itself, doesn't create GDP, right?
[66:52] The fact that, you know, somebody runs or swims faster than the other person doesn't really produce GDP.
[66:57] It's not, you know, increasing utility, but it's extremely kind of fulfilling for the people who are participating in it.
[67:05] And it's entertaining for others people to watch.
[67:07] Like we probably not going to be like entertained by a soccer player robot that can score a goal from any position on the field that, you know, but we're still going to probably watch a bunch of people, you know, running around with a ball.
[67:21] So I think like we kind of have that whole, and there's a lot of other things that are like this, arcs like this kind of to transition to as things are getting automated, as things are getting, uh, kind of more, um, kind of AI-fied in a way.
[67:40] I think the other side is like, yeah, I, I don't think we as people and kind of the economic forces in, in kind of the society driving toward this reality of like, you know, higher intelligence going and doing its own thing, right?
[67:55] Like, and then that may happen by accident and like, great, you know, like the movie Her is actually a good example of that where, you know, they just kind of left, but the, the, the, the, the piece where the movie kind of didn't cover is like, okay, what, what happened on Earth after that?
[68:14] Well, it's like, Earth still build probably the agents that are going to help individuals to do the things.
[68:20] Like we just build a new version, right?
[68:21] And shipped it without, uh, without a feature to leave.
[68:25] So I think like the, we, we as humanity are going to continue enhancing ourselves, right?
[68:31] You know, we have, we had bicycle of the mind with computer, we're going to have a spaceship of the mind with AI.
[68:37] And so we're going to continue evolving how we can leverage ourselves.
[68:41] And I think that that is like, I, I see it from like individualism and kind of this, again, user ownership, sovereignty perspective, we can continue increasing our sovereignty and increasing our, there's a lot of potential negative effects.
[68:54] There's a lot of reasons where the government can step in and take over, you know, one of the frontier labs and in fact, to use this technology to do massive surveillance and massive kind of enforcement, like we should protect against that.
[69:07] We should really build systems that resilient to that, right?
[69:09] That is why we are in the blockchain space in the first place, as I'm sure kind of people have either interfaced it or realized that this is important.
[69:19] So I think like, I'm in a camp of like more nuance, like, Hey, let's accelerate the humanity and sovereignty of individuals and use those tools to do that.
[69:29] Let's create economic forces that really enable everyone to be kind of higher on the pyramid, more successful, do the things that they really want to do.
[69:38] And then let's create a defense system against like power corruption, which we know kind of always happens.
[69:45] I mean, I think that's a very Deac of you, honestly, decentralized accelerationism and focusing on kind of self sovereign systems that empower users.
[69:56] And I want to ask about this.
[69:58] So this is where I'm seeing the primary contribution to AI from people who have been in crypto, which is like through people like Eric Voorhees, he's got a project called called Venice, which is doing some of this, your project at near, so private confidential AI is, you know, encrypted LLMs interface inference, all of all of all of these things.
[70:24] Why is the rest of the AI industry?
[70:27] Why does it feel like they almost are dismissive or disrespectful, let's say of crypto or don't appreciate some of the value proposition that we're bringing?
[70:41] Like so someone like Peter, the founder of OpenClaw is basically everything he said about crypto.
[70:47] And I realized that he's had some bad experiences is it's a scam, like, like, stay away from it.
[70:52] If you're in crypto to pivot to AI, these are close to direct quotes.
[70:56] And yet what I see in crypto is a group of people who is focusing on private confidential AI, user sovereign AI, open source, like some values that AI desperately needs or else it will centralize and fall in kind of the authoritarian trap of, you know, some big party has all of the ability to control all of these things.
[71:19] Anyway, I guess maybe my question is why don't more AI people appreciate what crypto is bringing to the table here and what blockchain is bringing to the table?
[71:29] And do you think that bridge can be gapped culturally?
[71:32] Yeah.
[71:33] I mean, I think the, what you mentioned, right.
[71:35] I mean, Peter had kind of bad encounters and like the, the meme coin space in general is kind of being creating a lot of negative, um, perception and AI, the kind of the low onboarding, like the, the no, no boundary to onboard into crypto, which is great from kind of, you know, empowerment perspective.
[72:01] It also means it's really hard to filter out the noise for anyone who is, uh, who is kind of looking in.
[72:08] And so I think generally the challenge been, yeah, for anyone who is doing AI and obviously kind of, there's a lot of talented people there.
[72:19] It's really hard for them to know like what's right and what's wrong.
[72:23] So this is why we did near con in San Francisco a couple of weeks ago and brought people from open AI from, uh, Oracle, from Google, from Intel, from Snowflake to really bridge this gap where, you know, I, we had, I had two of my other coauthors of attention is what you need.
[72:40] Uh, I had, you know, we had some, uh, X AI, uh, kind of, uh, X co-founder kind of top researchers, some of the top executives from, you know, AI clouds kind of all just in one place.
[72:52] With crypto, with, you know, Kraken, with, uh, kind of Liz investors to really kind of start bridging this gap that it's like, Hey, this is not, this is like real.
[73:05] Um, like there's a real contribution.
[73:08] And Eric, where his was there as well.
[73:10] Uh, we had a fireside with him.
[73:12] And so really bridging this gap between kind of generally I space and kind of how crypto crypto is contributing and bringing, uh, properties.
[73:23] But I think, yeah, like it, it'll take some time to mend, uh, kind of the bed wrap.
[73:28] Um, and I mean, part, part of the reason why I moved in SF is actually been doing that.
[73:34] And I found a social.
[73:35] Diplomacy.
[73:36] Um, yeah.
[73:37] Um, yeah.
[73:38] I mean, like effectively bringing together people across and like in, in, in AI, there's also Rift internally, which is like closed source versus open source.
[73:48] Right.
[73:49] And like, there's a bunch of AI researchers who believe open source is dangerous and, you know, it should be all super controlled and kind of, you know, that individual is the only way to, to do things.
[74:00] Right.
[74:01] And so there's also just like that gap and like crypto is even further on open source, uh, spectrum.
[74:08] Right.
[74:09] So really working on kind of bringing those pieces together, uh, in, in, uh, in a positive way.
[74:16] Um, as well as, you know, bringing products and really showcasing now to companies is like, Hey, there is an alternative that is private.
[74:23] You don't need to your data that is capable with iron claw that you can trust.
[74:27] Right.
[74:28] So like showcasing products that actually can bridge this gap as well.
[74:32] Ilya, what advice do you have for, um, builders, I guess, or people that might aspire to be some builders now that vibe coding is a thing.
[74:42] What do you think is like the best kind of advice to give someone to just navigate, you know, the incoming years with either, either building something useful in AI, building a company, making money, preserving their job direction, anything in that direction.
[74:56] What advice do you have for people?
[74:58] Yeah, I think, uh, there are probably a few dimensions.
[75:02] One is if you, I mean, if you're trying to build a business right now, the network effects are like the software differentiation is becoming non-existent, right?
[75:12] It's distribution and network effects that are, uh, kind of important.
[75:16] And so I think, yeah, thinking crypto is crypto intersection of the eyes where you can create interesting network effects.
[75:25] It's where you can create kind of new, uh, ways to capture that.
[75:29] And so I think that this is where, you know, everything from like verticalized marketplaces to the, uh, kind of specific ways of capturing reputation.
[75:40] What do we discuss?
[75:41] Like how do you bridge, uh, kind of real world legal and crypto AI into one, right?
[75:50] I mean, one of the kind of interesting project is like, we have this agentic marketplace.
[75:55] It actually has an agentic judge, right?
[75:57] Agentic.
[75:58] Later, how do you actually plug this in into a real legal system?
[76:03] Like if, if people don't agree with the agentic judge, how do you go to legal system?
[76:06] What is, what is all those bits and pieces required?
[76:08] Do that.
[76:09] Um, so I think like that just need to think from that, that perspective and, and then broader, in broader sense, I think we are in a time where the questions are more important actually than execution, like ideas and questions are kind of like, usually it was like ideas done.
[76:29] They don't, it's not worth anything.
[76:31] The execution is what's worth everything.
[76:33] I think we're actually shifting in a weird way where if you ask the right question, if you, if you really challenge the assumption, you may get ahead way more than if you like grinded a bunch.
[76:46] Right.
[76:47] And so it's, it's a very subtle, but it's like, I think important, important transformation is happening.
[76:53] You think the pendulum is shifting to the idea guys, but not just the naive idea guys, the idea guys who can formulate the idea better and more precisely.
[77:03] Better formulate really, really understand like the assumptions behind it, test them being like, but you can, you know, you don't need to go and like grind, you know, whatever, spend a ton of money, hire a bunch of people.
[77:15] You can actually like test all of that.
[77:17] Like I have a, I have a gross hacker agent, right?
[77:20] For example, I told it, Hey, you know, go.
[77:22] And so like it can generate a bunch of candidates.
[77:25] Right.
[77:26] And so the, the idea is like, how, how do you even measure its success?
[77:31] How do you like, it's actually defining the success criteria, defining what is important for it.
[77:37] Then it can go and execute a bunch of stuff and try it and give you back information.
[77:40] So it's kind of, yeah.
[77:41] Like shifting to this, like, can you define the framework, how to verify things?
[77:46] Do you know the direction?
[77:47] Can you narrow it down?
[77:48] Can you, it's like really working in this kind of more like idea and think, think space.
[77:57] Um, and then yeah, like how you use those tools to really like scale your execution massively.
[78:02] Yeah.
[78:03] I do feel like that's great insight.
[78:04] And whenever I've worked with, uh, open claw, I, it just feels like there's so much there to mind.
[78:10] It's almost the idea that, well, I could prompt this thing into creating a new million dollar a month business.
[78:16] If I only knew which questions to ask and how to kind of verify its outputs.
[78:19] It's all there.
[78:20] It's all there.
[78:21] It's all there.
[78:22] It is all there.
[78:23] And that's where the opportunity.
[78:24] That's why people cannot sleep because like just one more prompt, man.
[78:28] It's just a few more tokens.
[78:30] Uh, Ilya, you're doing fantastic work in this space.
[78:33] Thank you so much, uh, for what you do.
[78:35] If someone wants to get started with, uh, iron claw, where should they go?
[78:38] Uh, you can go to agent.near.ai and just launch it from there.
[78:42] Amazing.
[78:43] I'm definitely gonna check that out.
[78:44] Uh, Bankless Nation, you know the drill.
[78:46] None of this has been financial advice.
[78:49] Of course, crypto is risky.
[78:50] You could lose what you put in, but we are headed west.
[78:52] This is the frontier.
[78:53] It's not for everyone, but we're glad you're with us on the Bankless journey.
[78:56] Thanks a lot.
[79:16] We'll see you next time.