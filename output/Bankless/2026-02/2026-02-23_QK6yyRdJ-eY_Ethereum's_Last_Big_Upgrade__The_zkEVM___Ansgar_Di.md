---
channel: "Bankless"
video_id: "QK6yyRdJ-eY"
title: 'Ethereum''s Last Big Upgrade: The zkEVM | Ansgar Dietrichs'
published_at: "2026-02-23"
duration: "1:23:35"
word_count: 90600
---

# Ethereum's Last Big Upgrade: The zkEVM | Ansgar Dietrichs

[00:00] And ZKVM is this fundamental insight that what you can do is you can basically allow nodes to verify that a block followed all the rules without having to re-execute the block.
[00:13] It's a very non-intuitive thing, right?
[00:15] A blockchain by its nature is a very symmetrical thing.
[00:17] Every node basically does the same thing.
[00:19] Of course, you have block producers, but then every node kind of has to download, re-execute.
[00:24] You're duplicating the effort across the network.
[00:26] And now you're jumping to this, like, through this very fancy cryptography, you're jumping to this world where you still have the same effort to build a block, but then verification in a way is effortless.
[00:37] It has this magical compression element to it.
[00:40] Bankless Nation, I'm here with Ansgar Dietrichs.
[00:45] He's a researcher at the Ethereum Foundation.
[00:47] We're going to talk about the ZKVM today on the show.
[00:50] Ansgar, welcome to Bankless.
[00:51] Hey, great to be here again.
[00:53] Pretty ambitious subject, Ansgar.
[00:56] Ethereum has had this history of very big forks, hard forks that have upgraded Ethereum from this early primitive proof of concept where it started in 2015 to what it is today, which is fundamental infrastructure, the backbone of internet money and internet finance.
[01:12] We had the Merge, which did proof of work to proof of stake.
[01:14] We had EIP-1559 that upgraded Ether economics and transaction user experience.
[01:20] There's also 4844, which just enabled Ethereum's roll-up environment to become its best self.
[01:25] With each of these forks, they all represented this rallying cry for the Ethereum community.
[01:32] They were this, like, kind of grand unifying force of attention by the Ethereum community.
[01:37] And it allowed Ethereum itself to command attention from the rest of the world.
[01:41] The rest of the world paid attention to Ethereum when Ethereum had these forks, these incoming forks.
[01:47] The Ethereum was just loud.
[01:49] And I think these kind of represent Ethereum, some of Ethereum's best moments, when Ethereum has these kind of cultural shelling points for technological upgrades to what we consider in the Ethereum community to be critical social infrastructure.
[02:06] Now, I think, Ansgar, and I want to suss this out, this topic out with you, that there is another fork on the horizon.
[02:14] It's not soon.
[02:15] It's not this year.
[02:16] It's likely not next year either.
[02:17] But nonetheless, it is there on the horizon.
[02:19] And I think it deserves attention.
[02:21] I think it deserves the treatment that the Ethereum community has given previous forks.
[02:26] And I think in addition to all of the valuable things that we got from the three forks that I just mentioned, this one is actually the biggest upgrade that Ethereum will ever experience because it relates to users more than any of the three forks in the past.
[02:41] And that is the fork that introduces the ZKEVM to Ethereum.
[02:46] Now, Ansgar, these are the sentiments that I want to start this podcast off with.
[02:50] Before we get into what is the ZKEVM and all the technical details about it, I just want to give those sentiments to you and have you reflect upon them before we kind of dive into the technicals.
[03:01] I personally share your excitement on this topic.
[03:04] I really think that it's one of those changes that are really Ethereum at its best.
[03:10] It's one of those really ambitious technical projects that I think Ethereum is in a unique position to deliver.
[03:17] It will have a huge impact primarily through scaling.
[03:21] But in many ways, I'm sure we'll talk about all of this.
[03:25] And I really think it's something we can look forward for, we can be proud of.
[03:34] And yeah, I'm excited to talk about the details.
[03:38] I will say, by the way, you said hard fork.
[03:41] And the interesting thing here is like similar to if you think back at the merge, right?
[03:43] We had first the launch of the beacon chain, which was one moment in time.
[03:47] And then we later on had the mergers, like two separate moments in time.
[03:49] And I think similarly, maybe even to a larger degree with ZKEVM, as we'll discuss, it actually, it has this nature of it's an ongoing transition that is basically about to start.
[04:01] Then we will have the main hard fork and then it will continue after.
[04:04] So it's much more like a ongoing transition.
[04:06] But yeah, let's dive in.
[04:09] So it is the introduction of an era of Ethereum rather than an acute hard fork.
[04:14] And I think the ZKEVM era will be, has the potential to be Ethereum's best era because of what the ZKEVM does for Ethereum.
[04:23] So let's stop hyping it up and start to get into the technical details.
[04:27] What do we need to know about what a ZKEVM is?
[04:31] What is it?
[04:31] And then we can talk about like why, what it is that's so significant to Ethereum.
[04:35] Yeah, so I think, you know, to understand this, like really kind of you have to start from the problem statement, right?
[04:40] So ZKEVM really arose in the context of scaling of and basically the fundamental point is that a blockchain, if you run a blockchain and you have these three primary constraints, you have the data, right?
[04:56] You have to first like any new block you created has to get to the user.
[05:01] Then you have the IO, you have to like then go to disk, you have to get all the data you need to actually like then verify the block.
[05:06] And then you have the actual verification, the execution, the compute, right?
[05:09] So those are like the three main constraints, the bandwidth, the IO and the compute.
[05:14] That's any blockchain, no matter the design, those are the main constraints.
[05:18] And so if you want to scale this, you can just do the thing where you take that and you just scale it up.
[05:24] And we'll talk about this in a bit.
[05:26] That's actually to some degree what we're doing in the short term.
[05:29] And that's what many other chains have been doing.
[05:31] That's a very natural thing.
[05:32] But you do run into limits.
[05:33] You do run into tight limits.
[05:35] And so ZKVM is this fundamental, like it comes from the cryptography side, these snugs, zero knowledge proofs.
[05:45] And it is this fundamental insight that what you can do is you can basically allow nodes to verify that a block followed all the rules without having to re-execute the block.
[05:58] And that's, again, like that's something that's, it's a very non-intuitive thing, right?
[06:03] Normally it's, a blockchain by its nature is a very symmetrical thing.
[06:07] Every node basically does the same thing.
[06:09] Of course, you have block producers, but then every node kind of has to download, re-execute.
[06:14] You're duplicating the effort across the network.
[06:16] And now you're jumping to this, like, through this very fancy cryptography.
[06:20] You're jumping to this world where you still have the same effort to build a block, but then verification in a way is effortless.
[06:27] It has this magical compression element to it.
[06:31] And then specifically what's so important in the L1 context is the real-time element to it.
[06:38] So ZKVM just allows for this compression.
[06:41] And for example, many listeners, I think, will already be familiar with the concept of ZK roll-ups, right?
[06:46] So those have been around for a while.
[06:47] And that actually was a huge first jump in this technology, which just allowed for this compressed ZK verification in the first place.
[06:55] But so far, this is done in an asynchronous way.
[06:58] So meaning you have your L2 blockchain that, you know, it's its own chain, basically, and it keeps progressing.
[07:04] And then afterwards, with some, you know, up to several hours of delay, you come and you basically compute over a long time these proofs, and then you bring them to the chain.
[07:14] And what now is the second huge jump here is to go from this very asynchronous, delayed process to a proving, a verification loop from block creation, proving verification that all happens at the same speed of the blockchain synchronously.
[07:31] So like within a single Ethereum slot right now, that's 12 seconds, we will bring that even further down.
[07:35] You have this entire loop, closed loop within that short amount of time.
[07:39] And so basically, that's many orders of magnitude of performance improvement.
[07:42] And that really is what unlocks all of these huge gains for the L1.
[07:47] Galaxy operates where digital assets and next-generation infrastructure come together, serving institutions end-to-end.
[07:53] On the market side, Galaxy is a leading institutional platform, providing access to spot, derivatives, structured products, DeFi lending, investment banking, and financing.
[08:00] With more than 1,600 trading counterparties, Galaxy helps institutions navigate every phase of the market cycle.
[08:06] The platform also supports long-term allocators through actively managed strategies and institutional-grade staking and blockchain infrastructure.
[08:12] That scale is real.
[08:14] Galaxy has over $12 billion in assets on the platform and averaged a $1.8 billion loan book in late 2025, reflecting deep trust across the ecosystem.
[08:22] Beyond digital assets, Galaxy is also building infrastructure for an AI-powered future.
[08:26] Its Helios Data Center campus is purpose-built for AI and high-performance computing, with more than 1.6 gigawatts of approved power capacity, making it one of the largest sites of its kind.
[08:36] From global markets to AI-ready data centers, Galaxy is serving the digital asset ecosystem end-to-end.
[08:42] Explore Galaxy at galaxy.com slash bankless, or click the link in the show notes.
[08:46] Euphoria brings one-tap trading to the palm of your hand.
[08:49] Built on MegaEth, Euphoria takes real-time price charts and projects it over a grid of squares.
[08:54] You tap the squares that you think the price will enter in just 5 to 30 seconds in the future.
[08:58] If the price goes into that quadrant, you can pocket anywhere between 2 and 100x your trade.
[09:03] No other application helps you trade faster and with more leverage on market-driving events, like FOMC meetings, presidential speeches, or global macro events.
[09:11] Thanks to MegaEth's real-time blockchain, Euphoria is the way to get real-time price interactions with the market.
[09:17] On Euphoria, you'll be able to compete with friends using Euphoria's real-time social trading experience, allowing you to go head-to-head with your friends.
[09:24] It's a great party trick if you project the app on a TV.
[09:26] It'll be like the Mario Party of derivatives.
[09:29] To trade on Euphoria, people can deposit stablecoins from any chain or do direct fiat transfers, and everything gets converted into MegaEth's native stablecoin, USDM, in the background.
[09:38] Check it out at euphoria.finance and download the app or find it in Telegram as a mini-app.
[09:44] In 2024, emerging markets generated over $115 billion in annual yield for investors, with yields ranging between 10% to 40%.
[09:53] These are some of the highest, most persistent yields on Earth.
[09:56] The problem?
[09:57] DeFi can't access them.
[09:58] BRICS changes this.
[10:00] Built on MegaEth, BRICS takes emerging market money markets and sovereign carry and turns them into composable primitives you can access straight from your wallet.
[10:08] While DeFi investors earn 3% to 6% on stablecoins and T-bills, institutions have been harvesting 10% to 50% yields backed by sovereign monetary policy.
[10:16] BRICS connects these worlds with institutional gray tokenization, local banking rails, compliance across jurisdictions, and real-time stablecoin settlement.
[10:24] BRICS does the heavy lifting so DeFi can finally access real collateral and structured products on top of real world yield.
[10:30] Even the best carry trades can be within reach.
[10:32] BRICS brings DeFi's promise to the emerging world and brings emerging market yield to your wallet.
[10:37] Let the yield flow with BRICS.
[10:39] Maybe going back to just like what makes a blockchain a blockchain, Bitcoin had this fundamental insight of the way that we get rid of a leader in a blockchain is that everyone checks the legitimacy, the authenticity, the correctness of everyone else.
[10:57] And so when some Bitcoin miner mines a block, but it finds the correct hash and it proposes that block, everyone else in a network doesn't trust that leader.
[11:09] They re-execute all of the same work to verify it for themselves.
[11:14] And that's the way that Bitcoin discovered the way to have a decentralized network is everyone's checking everyone else.
[11:20] And that re-execute word has just been the status quo for all blockchains.
[11:27] And the way that that impacts blockchains, all blockchains to this day, is that it kind of is hamstrung by the slowest node in the network.
[11:38] Or at least there is some requirement for computation that every blockchain has that, you know, if you aren't at least this fast, you can't keep up with the network because you can't keep up with executing all the everyone else's work.
[11:53] And now, you know, some blockchains have different opinions as to like how much requirement you have.
[11:57] Bitcoins is very low.
[11:59] Ethereum has also been a very low requirement because we want to be decentralized.
[12:04] You know, as you said, like, you know, some chains like Solana or other very fast chains have had a higher opinion as to the computational requirements it takes to do the re-execution.
[12:13] But nonetheless, all blockchains to this day are re-executing all of the same work.
[12:18] And it's redundant.
[12:19] It seems unnecessary.
[12:20] It seems like, is there a way where we can not do all of that extra work and still have a blockchain?
[12:26] And a parallel to that, as you said, with like the Ethereum layer twos, what we understand is that there is a way to not do this.
[12:35] And that is with ZK proofs.
[12:37] So in addition to the technological progress of blockchains as a whole, we can make them more efficient.
[12:42] We can, you know, we can juice some of the throughput.
[12:45] But on a parallel path, there are cryptographic algorithms that instead of allowing or forcing everyone to do the re-execution, you can simply verify a cryptographic hash, a cryptographic proof.
[13:01] And that part is trivial.
[13:03] It's easy to verify.
[13:05] It's hard to produce in the same way a block in a blockchain is hard to produce, but it's trivial to verify the correctness of a cryptographic proof.
[13:14] And that's kind of the trick.
[13:16] That's where we remove the re-execution.
[13:19] A great Elon Musk quote here is, the best part is no part at all.
[13:25] And what a cryptographic proof does is it removes the whole part of re-execution.
[13:30] So blocks in a blockchain get executed once, and then no one has to actually re-execute it.
[13:37] They can just trivially verify it, which allows for a lot of redundant work to get removed from the system.
[13:43] And that allows for just work being constrained down to one block producer.
[13:47] And then everyone else is just like, thumbs up.
[13:49] That is correct.
[13:50] And we really take off the brakes off of a blockchain system.
[13:54] Now, the reason why Bitcoin wasn't built like this in the first place, the reason why Ethereum wasn't built or any other blockchain wasn't built like this in the first place was, you know, technological progress along cryptographic hashes also needed to mature.
[14:08] Maybe you could like take everything that I just said and run with it, but also talk about just like the technological parallel path of cryptographic proofs as they've been progressing alongside blockchains.
[14:19] Yeah, absolutely.
[14:21] So actually, just to start with where you started with the Bitcoin example, because some listeners might have heard this and might have been like, hey, actually, isn't there this asymmetry as well where a miner does all this like very expensive work, but then not every other node has to like redo the same mining, right?
[14:36] Indeed, in the mining process, there's the same efficiency like asymmetry.
[14:41] And that's actually, it's a very common trick in cryptography where basically like you try with mining, you try all these different hashes, you find one hash that has enough of like leading zeros.
[14:50] That's how the difficulty in Bitcoin worked.
[14:51] And then you can just show people and it's very cheap to verify.
[14:55] So Bitcoin on the consensus mechanism side already uses a similar trick, right?
[15:00] But on the actual content of the block, right?
[15:02] So like what is in a block, in a Bitcoin block, it's all the transactions.
[15:05] Each transaction comes with a signature.
[15:07] So you have to like actually like verify the signatures.
[15:09] You have to say, okay, balance was moved from this account to that account.
[15:12] All of the actual operations of the blockchain, that's the re-execution part, right?
[15:16] So Bitcoin does get, has this like, again, because this is a very typical trick in cryptography that you have this like asymmetry of generation versus execution.
[15:24] It uses that for mining because that's easy to do with proof of work.
[15:28] It's very, very hard to do this for the actual operations within a block.
[15:32] And so now this is what basically the main unlock here is that basically now we're bringing the same efficiencies that people are used to from this like one miner, everyone can verify easily.
[15:43] We're bringing that same efficiency to the entire block in block.
[15:47] And of course, on Bitcoin, the actual Bitcoin block is very small.
[15:50] It's a very simple operations on Ethereum because you can run smart contracts and we are massively scaling the throughput.
[15:56] It's much more complex.
[15:57] Like the vast majority of the overhead in processing and following the chain is not the consensus part, not the proof of stake part, but it is this, the actual contents of a block.
[16:07] So what has changed on cryptography?
[16:09] Actually, my friends from the Xerox PARC team, they are like one of those cryptography research labs.
[16:17] They always talk about, I think they call it, maybe I'm getting this slightly wrong, but they call it the first generation of cryptography and the second generation of cryptography.
[16:24] What was the first generation of cryptography?
[16:26] It was basically handcrafted algorithms for very specific use cases.
[16:33] So a signature algorithm or a hash function or anything that basically, it fulfills a very specific purpose and you can use it in a very specific context.
[16:42] And those are amazing, right?
[16:44] And that's been like the story of cryptography for the last 50 years, right?
[16:47] It's basically like a more sophisticated special purpose mechanisms.
[16:52] And those were already very mature when, say, Bitcoin started, right?
[16:55] This is why they were able to just take the concept of hash functions off the shelf and you can do amazing things, signature mechanisms, all that kind of stuff.
[17:03] What is like very new, it basically started, I don't know, a decade ago or something like this, probably academically a little bit earlier.
[17:09] I'm not actually a cryptography expert myself, so I don't know the exact kind of like early story there, but that's basically like cryptography 2.0 in a sense.
[17:17] It's general purpose cryptography.
[17:19] It is basically now the ability to make cryptographic statements about arbitrary computation.
[17:24] Instead of having to like handcraft it for a specific use case, you're now, you're going to this general purpose world.
[17:30] And this is like a huge leap because it means that instead of like just, say, signing a message, you can prove whatever you want.
[17:36] And anything Turing complete, anything that you, any execution whatsoever, you can now compress, you can make a cryptographic statement over.
[17:44] And that was a giant leap.
[17:48] It was, I think, only really, it was pulled from academic theory to feasibility, I think, through a lot of funding that came from the blockchain space, of course.
[17:59] It's really incredible progress.
[18:00] And that progress, I think, I would think of it as several stages.
[18:03] So one was just, not just, one was what we saw with ZK roll-ups.
[18:10] And then, of course, already prior to that, special purpose chains like Zcash, right?
[18:13] Was just the ability at all.
[18:18] You have a protocol and you can make a proof of it.
[18:21] You can basically, you can prove that a block of a blockchain is valid.
[18:27] What we've seen since is like this progression of the tech stack.
[18:31] So, for example, all of these earlier stages, like, again, Zcash, early ZK roll-ups, what they all did is they basically, they handcrafted the rules of the chain that they were trying to verify into like very low level, like, it's called circuits.
[18:50] It's basically like, you basically express it in like very low level constraints that you then make these your knowledge proofs about.
[18:56] And where we've been going from there is now we have this, and you can really, it's really, it parallels the early progression of computers as a whole, right?
[19:06] We went from, you have to specify, you have to manually specify every individual system you want to prove.
[19:11] Instruction, yeah.
[19:12] Yes, it's like this set of constraints of circuits.
[19:15] And it basically went from there to introducing, and it's such an elegant idea, but it's crazy that it works.
[19:24] It's just introducing this intermediate instruction set.
[19:27] So, it's called an ISA, instruction set architecture, and you can think of it like how a processor in a computer has instruction sets.
[19:35] So, x86, for example, right?
[19:37] Like Intel or ARM or whatnot, right?
[19:38] Basically, it's what instructions does your processor understand?
[19:43] And the way these modern ZK systems are now built is you pick one of those instruction sets, like the one that is actually becoming the standard in Ethereum right now is RISC-V.
[19:56] RISC-V is similarly, in principle, it's just like a list of operations that your processor could do, right?
[20:02] Like it's often run in a virtualized way, so it's not actually run on real RISC-V hardware.
[20:06] It's mostly run in a virtualized kind of way, but basically it's just like a list of instructions.
[20:11] And then you then write zero-knowledge provers that can just prove arbitrary RISC-V code.
[20:18] So, you're just saying like, look, give me any RISC-V code, and I just have this machinery that can make statements, cryptographic statements about it.
[20:24] And what that now unlocks is instead of having to handcraft like the early ZK EVMs, they were literally handcrafted EVMs inside of ZK systems.
[20:32] Now, you can just literally compile.
[20:35] You can just take basically, basically, you can take an Ethereum client, instead of compiling it to whatever your local machine has as an instruction set, instead of compiling it to x86 or something, you're now just compiling it to RISC-V, and then you just get the ZK proving for free.
[20:51] And RISC-V, that's just like a typical kind of endpoint for compilers, right?
[20:57] So, basically, you're modularizing the toolchain, and of course, that's only possible now with all the efficiency gains, because, of course, you're losing some benefits of handcrafting all the optimizations.
[21:07] But this really, it's a phase change from how feasible it is to do this for just like big, complex projects.
[21:14] And so, really, the way Ethereum does the ZK EVM is, again, of course, the real world is a bit more complex, but in principle, you can really think of it.
[21:21] We take the existing Ethereum clients, and we just compile them to RISC-V, and then we just have a provers that specialize in making proofs over RISC-V.
[21:30] And that's just, it's really amazing how far the industry there has gone to make that feasible.
[21:36] And then the last jump, the last big kind of conceptual jump from there to this is becoming feasible for us is the real-time element.
[21:43] So, we arrived at that world, and you could do that within an hour.
[21:48] I mean, sometimes if the block is actually convenient to prove, maybe you can get it down to a few minutes, whatever.
[21:53] Like, that's the world that we used to be in.
[21:54] And then we basically, we have had this massive industry collaboration effort that started like a year, year and a half ago with Justin Drake really like pushing super hard on this.
[22:05] And these teams, and this is really mostly driven by teams outside of the Ethereum Foundation, these teams have done an absolutely amazing job.
[22:12] And I would say the last year was really the year of performance, of real-time performance.
[22:18] And throughout the last year, teams just kept pushing this down orders of magnitude.
[22:23] And now, we're at the point where you can, we are starting to achieve the target zone.
[22:28] So, like, we are actually able to prove, consistently reliably prove a full Ethereum block within five seconds, something like that.
[22:37] And that's basically the promised land.
[22:39] Because now we have all the technological building blocks, and now we can talk about the rollout and all these things.
[22:44] But we have all the, like, from the cryptography side, we now finally, for the very first time ever, we have all the elements we need to run a general-purpose blockchain at real-time proving speeds.
[22:54] And that's something that has never been possible before.
[22:56] I really like the idea of there has been this, you know, three parallel paths of computing.
[23:01] First, starting with computers, where they were first narrow, and then we were able to make them generalized, and then we were able to make them generalized and fast, which is where, you know, modern computers are now to this day.
[23:14] And then we created blockchains, you know, virtualized ledger-based computers in the, you know, in the sky, decentralized systems.
[23:21] They started narrow with Bitcoin, and then we learned to generalize them with Ethereum, and then we learned to generalize them and make them fast with many other smart contract chains.
[23:31] And now we are doing the same thing with cryptography.
[23:34] Started narrow with cryptography, learned to make it generalized, and now we are making them generalized and fast.
[23:40] And that generalized and fast unlock on the computing tech tree of cryptography is now being able to be taken and bestowed into Ethereum.
[23:51] Which is what we're going to talk about for the rest of this episode.
[23:52] So, now that we have the ZKE VM, and it's in the Ethereum blockchain, and, you know, it's up and running, what does that actually change with Ethereum?
[24:02] When we get to this point, how does Ethereum actually change?
[24:05] Right. So, of course, we're not there yet, but that's kind of, that's where we're going.
[24:09] And so, why is this useful?
[24:10] So, coming back to scaling, right, I said that there's basically these three main elements of scaling.
[24:15] There's the bandwidth, the IO, and then the actual compute.
[24:21] Now, the amazing thing about real-time ZKE VM is that it actually is the core of a broad, like, the way I would say it is, like, it helps us scale all three of these, but not just on its own.
[24:32] But it's basically, it's the unlocking piece that allows, that basically enables a broader transition that addresses all of these elements of scaling.
[24:40] And so, that's why when we talk about ZKE VM, to me, it's more like the most exciting element of this broader change.
[24:46] And that's why when you said at the top of the podcast, this might be the biggest change ever, I would agree, not just the ZKE VM itself, we'll talk in a second about statelessness, about data availability sampling, like, all these things come together to unlock this.
[25:00] So, let's take it step by step.
[25:01] So, the one of those three constraints, the one immediate impact you get is on the compute side, right?
[25:08] So, because that's the nature of ZKE proofs, right?
[25:10] You basically, you're able, with very little compute effort on the verification side, to verify arbitrary length execution.
[25:18] So, no matter how much you fill the block, now, of course, we can talk about constraints, there's still block building, some node, somewhere needs to do that.
[25:25] So, it's not, doesn't give you literally infinite throughput, but basically, right?
[25:29] Like, you can have whatever, like, length of computation you have, you can compress it down into a constant size proof, and then you can verify that with just very little compute.
[25:38] So, compute scaling, that's the, in a way, the easiest one.
[25:41] That's the one that you get very easily.
[25:43] Now, you look at the other two, and you're saying, okay, how does it impact I/O, right?
[25:50] So, historically, traditionally, when you execute an Ethereum block, what you do is you start executing, you do some compute, at some point you want to load some state.
[25:58] Actually, already at the beginning of a transaction, you want to, you know, you need to load your account, you need to load the account of, that you're calling into, that you're sending ETH to.
[26:06] So, you basically, you immediately need to go to disks, right?
[26:09] So, you have this intermixing of, sometimes you go to disk, you load value, sometimes you do some compute, then you go to disk again, it's like this, this intermixing.
[26:16] One actual change to Ethereum that we're already doing before ZKDM, it's called block-live-access-list.
[26:22] So, it allows us to, it basically, it adds some annotations to a block of, like, this is the data you'll need.
[26:28] So, actually, what happens now is that you actually go to disk at the very beginning.
[26:33] You bring all the data and then you can do the execution.
[26:36] But you still have this element of having to go to disk both before the block and then again after the block to go and, like, be okay, but what's, you know, like, we have to update all the values and then we have to also, like, compute what is the new state root.
[26:51] So, how does it look with ZKDM?
[26:54] Well, there's a few things that are fundamentally, like, improved by ZKDM.
[26:58] So, the important part is that ZKDM basically already takes in, as part of the claim, it's like, hey, assuming the blockchain was in this state and I apply these transactions, now then the next state is this.
[27:11] So, basically, like, you no longer need to go and load the data from, the values from disk.
[27:16] So, basically, you're saving this I.O. on the load side naturally.
[27:20] And then the thing that you normally still have to do is you have to, like, go and still write the updates, right?
[27:27] So, if you still have the state of Ethereum, so after you verify the block, you still have to go and say, okay, these values change, right?
[27:33] So, you have to go and apply that change.
[27:35] One, that's no longer in the critical path.
[27:37] So, you can do that after you've already finished verification.
[27:40] So, if you have valid data, you can already vote.
[27:41] You can, like, say, ah, this block was valid.
[27:43] And then afterwards, I go and actually apply the updates.
[27:46] So, in terms of, like, what is the current price of this Uniswap pool or what's the balance of this account, right?
[27:51] Like, I might only go update this on disk after I already know that the block is valid.
[27:56] So, that's a natural benefit you get.
[27:58] But if you want to push it further, we have to, and this is what I was saying, like, this is one of those changes that is enabled by ZKVM, but it's its own change.
[28:06] It's a stateless Ethereum or partially stateful Ethereum.
[28:11] So, what does that mean?
[28:11] Well, instead of, like, today, any node in Ethereum network basically has to have the full state.
[28:19] And that's, with re-execution, that is unavoidable, right?
[28:23] Because if you want to verify a block, you have to go and, again, load all the data.
[28:27] You have to have it all locally.
[28:28] And once you have ZKVM, that becomes optional because you don't actually need the data local to double-check the validity of the block, right?
[28:36] So, what you can do is you can, in principle, what you could do is you could throw away the entire data, right?
[28:41] So, you can basically just, you can only keep, like, this root commitment and you can just always update the root commitment and that's it.
[28:47] In practice, what you'd want is, because Ethereum nodes have multiple functions, they also operate the Ethereum mempool, they have to understand validity of transactions in flight, all these kind of things.
[28:57] What you'd want to do is you don't want to run fully stateless.
[29:00] You want to run in what we're calling partial statelessness.
[29:03] So, for example, there's this proposal called VOPS, Validity Only Partial Statelessness.
[29:08] So, it means you specifically have a subset of the state and that can be defined by several different rules.
[29:13] It can be, say, the balances of all the accounts or it can be, I don't know, if you are specifically interested in some state that belongs to you as the user or something, you can define what state you're interested in.
[29:22] But, basically, now you can keep a subset of the Ethereum state and that's totally safe because of ZKVM, right?
[29:31] And you only have to apply the diff, you only have to go to disk, you only have to have the IO overhead of updating that subset.
[29:37] So, that's the second, basically, you have ZKVM for compute, now you have partial statelessness for more optimized IO and also, by the way, for keeping your disk size contained.
[29:48] We'll talk about state growth maybe towards the end, but basically, you know, so you don't have to have, like, a huge disk.
[29:54] And then it leaves the third one, which is bandwidth, right?
[29:58] So, and how do you actually, like, keep scaling the chain now with the ZK system while actually keeping bandwidth requirements the same or even reducing them?
[30:10] Well, that's yet another separate trick that's also, again, enabled by ZKVM, but it's separate.
[30:15] And that is, you no longer actually need to download the full block.
[30:20] And that makes sense, right?
[30:22] Because you kind of, you get the ZK proof, you have to download the proof, and the proof tells you, hey, assuming there is a block with this hash or something, once I apply the block, this is the result.
[30:33] And that's proven.
[30:34] So, the only thing you need to know about the block is that it exists.
[30:38] And that's a bit of a nuanced thing.
[30:39] Like, why do you even need to, I mean, someone clearly must have created it, otherwise they could not have created the ZK proof.
[30:43] So, why do you have to verify that it exists?
[30:45] Well, that's for the nuanced reason that you can otherwise withhold the data.
[30:48] Like, that's also the same for, that's why, for example, we even have blobs in the first place, actually, for L2s.
[30:53] It's the same story.
[30:54] You have to publish, you have to basically prove that the block was published.
[30:58] So, anyone can access it, and anyone can get access to the transactions that were applied, basically.
[31:05] So, but what you can do is, I mean, that's, again, where, like, the synergy with the L2s, it's just a beautiful story.
[31:09] We've already built out specialized functionality for verifying the existence of data very efficiently without downloading it all.
[31:18] It's called data availability.
[31:19] It's called blobs, right?
[31:20] So, what we will do is we'll take the Ethereum blocks, and we'll just, we'll just basically become our own rollup, in a sense.
[31:25] We're putting the data into the blobs, it's called block and blobs, BIP, and with that, now all an Ethereum node has to do is just sample.
[31:35] Sample the data, and we'll be in the progress of making that more and more efficient, because we want to provide more and more data for our L2 partners.
[31:41] And that now naturally also benefits ourselves, because now you can have more and more, like, bigger and bigger blocks, while keeping the footprint in terms of bandwidth also very constrained.
[31:50] So, now, you're right, coming back, we have ZKVM, and we have partial statelessness, and we have block and blobs, data availability sampling.
[31:57] Together, they scale bandwidth, they scale I.O., and they scale compute.
[32:02] And that is how you basically, like, use all of these elements to scale the blockchain.
[32:06] And then there's some nuances, you don't get everything for free, you have state growth, we can talk about state growth, that we have to separately address.
[32:13] And you have things like being able to efficiently sync an Ethereum client, there are things like being able to efficiently run an RPC node, you know, like what Infura is doing, these kind of things.
[32:25] So, there's more to scaling than this, but the core story is that you have these three constraints, and ZKVM directly and indirectly addresses all three.
[32:33] You zoomed in on each one of those three, and, like, as you just said, you put those three together, that's how a blockchain becomes a blockchain, and we improve all three of those things.
[32:41] I want to zoom out and really focus at that level of advantage.
[32:47] When we reconstruct how a blockchain becomes a blockchain on, like, all three, comprehensively, you really kind of said it when you said Ethereum uses its own data availability to be a ZK roll-up.
[33:00] As I understand it, the ZK EVM, when it is up and running and operational and, you know, fully fleshed out and forked into Ethereum, the Ethereum layer one has the performance of a blockchain that is a ZK, that would, like, be a ZK roll-up.
[33:16] In fact, it maybe even is a ZK roll-up, it just also is a layer one itself.
[33:24] And so, we get all the performance benefits of roll-ups, we get to ZK everything, which unlocks the brakes, undoes, takes off the brakes on the Ethereum layer one, and we already have the infrastructure needed with the data availability sampling for this to get done.
[33:41] And so, from a performance perspective, the Ethereum layer one, which is known to be a slow, antiquated, you know, expensive blockchain to do computation on, upgrades itself to have the performance properties of a ZK roll-up.
[33:57] Is that a true statement that I just said?
[33:59] Yeah, I think that's right, and I think, like, just, I think it's important to understand, like, why even does Ethereum, like, why is Ethereum so slow, right?
[34:12] Like, if we ask that provocative question, the one really important element is that core to Ethereum's design philosophy is this guarantee that Ethereum never wants to compromise on, which is, like, easy verifiability and auditability.
[34:28] So, the world that Ethereum always wants to be in is that anyone that wants, any user of Ethereum can easily, if they want to, verify or audit that the protocol is following the rules.
[34:41] And why this is so important, like, people are always like, well, but in practice, many users don't do it, and, like, other chains, yes.
[34:47] Like, for example, if you're trying to join one of those high-performance chains, it's actually, it's really, really hard to run a full node for one of those chains that scale just by increasing hardware requirements rapidly.
[34:58] Because not only is it, do you need a heavy machine, but often, you don't, you can't even, you're not even allowed to join the peer-to-peer network, because it's so performance sensitive that they have to, like, have white lists for who even is allowed, which nodes are even allowed into the network, because otherwise they are just too brittle, right?
[35:12] And they just immediately collapse.
[35:14] So, basically, and why does it matter?
[35:17] Because I think people think about proof of stake always in this, like, well, there's validators, and they vote on what's the current state of the chain.
[35:23] In Ethereum, validators get, basically, like, get handed the current rules of the chain by the community, right?
[35:30] Like, and any hard fork is basically a social decision of, hey, it's a social governance act.
[35:35] The Ethereum community decides that now there are new rules to the chain, and the validators only vote on, like, okay, given those rules, like, which blocks did I see?
[35:44] Which blocks follow the, it's a very, it's a very, there's no, there's no individual decision that didn't attest to any theorem that makes, right?
[35:53] They just, they just watch the chain, and they just attest to what they see.
[35:56] In other proof of stake chains, while in principle, that should be the same thing, what in practice happens is that because any non-validator user of the chain is just a light client, because you can't just participate in the chain, you, basically, any user in those chains just trusts the majority of validators.
[36:14] So in practice, those validators determine what the rules of the chain are, right?
[36:17] Like, in a, in a chain that does not center verifiability, validators de facto control what the rules of the chain are.
[36:24] Like, if the majority of validators want to run a different set of rules, they can do that.
[36:27] In Ethereum, that's not the case.
[36:29] Validators can't accept or reject a fork, they can just make a fork of their own.
[36:32] They just get handed the rules by the community, and the ultimate power always lies with the community, right?
[36:37] So, like, that's why, that's why, like, verifiability, auditability is so core to Ethereum, and that's why we have been historically slow to embrace scaling, because that would endanger that property.
[36:50] And now, with ZKVM, we have this magical way of, of getting the best of both worlds, getting the full verifiability and the full performance.
[36:58] And although I will say, all of this is a bit too black and white, actually, what's been happening, so, for example, I'm not actually, like, I'm personally, while I'm involved with our ZKVM work, we have experts.
[37:10] We have Justin, who's been on the podcast before, often, many times.
[37:13] We have Kev, who's doing absolutely amazing work there.
[37:16] We have many people there that full-time work on this.
[37:19] And I'm actually focused much more on short-term scaling.
[37:23] And so, while it is true that with traditional scaling, there's, like, a limit that you can reach, and otherwise, you basically, you have this fundamental trade if you can't escape.
[37:34] Ethereum, historically, has been very much in this mode of, well, we're working towards this eventual end state, you know, and we know we want to eventually do ZK, so, you know, we'll focus on that.
[37:43] And as of, like, say, a year, year and a half, two years ago, I think the mindset on Ethereum has shifted a lot towards saying, look, we're now in this moment in time.
[37:54] Real-world adoption is here, right?
[37:56] Like, it's no longer this future thing that we're building towards.
[37:58] So, we have to, like, now, and it's actually, it's really, it's a very, like, non-trivial thing.
[38:04] We have to find the right balance between still working on these, like, Manhattan projectile-type jumps, like, real-time ZKVM.
[38:11] I really, I think, I really, like you said, like, I think it's the biggest thing Ethereum probably will ever have done.
[38:16] But we can't just wait for another three years for this to arrive.
[38:20] Like, we have to do things now.
[38:21] And so, this is why I think we actually, like, we're now, scaling is this perfect example.
[38:25] We have this really good hybrid approach.
[38:27] The next, like, we started last summer, we're saying ZKVM is three years out.
[38:31] And we will, in a second, I think, talk about more the sequencing of the exact law.
[38:34] But we don't want to wait three more years, right?
[38:37] This is what the old Ethereum would have done.
[38:38] What we're actually doing is we are, we now, we came up with this scaling plan.
[38:43] And it's a very continuous, smooth function.
[38:46] So, you can, our goal is basically, we have this rule of thumb.
[38:49] We're saying our goal is 3x scaling every single year.
[38:52] So, we are increasing the throughput of the Ethereum blockchain by roughly 3x every year.
[38:58] This is more of, like, a goal, an ambitious statement.
[39:02] It's not clear that every single year we'll be able to hit that.
[39:04] But I think we see a path, at least.
[39:06] It's a possible outcome.
[39:08] And in practice, the first three years of that scaling are with traditional means.
[39:16] And then, from that point on, basically, we have the smooth handover into the ZKVM paradigm.
[39:21] So, it's not all just black and white and Ethereum is only doing ZKVM.
[39:25] But actually, now, I think we have the best of both worlds now.
[39:28] We have, like, the next two, three years, we are doing this ZKVM in parallel.
[39:32] But we're still doing the traditional scaling.
[39:34] And then we jump into the ZKVM paradigm.
[39:37] And so, that means if you're a builder and you're considering building on Ethereum L1, you have this, like, instead of having to, like, exactly think, okay, one is this hard fork and what is the exact...
[39:44] No, you can just say 3x every year.
[39:45] You look at the throughput today.
[39:47] And you can just, like, very simply calculate, like, you know, what throughput needs do I have?
[39:52] Is the L1 a good fit or not?
[39:53] It's a very simple story.
[39:55] But under the hood, it has this, like, these, like, two synergistic elements to it.
[40:00] Sorry, that was a long answer there.
[40:01] Yeah.
[40:02] Well, the idea is that we're pressing the gas on scaling on multiple fronts, not waiting for the Manhattan project of the ZKVM, which, you know, the ZK EVM has been in the Ethereum roadmap since genesis, I think.
[40:16] Like, we've understood theoretically of the possibility of turning the EVM into a ZK algorithm.
[40:24] And, you know, we understood that theoretically back in 2015.
[40:28] Now we're in 2026.
[40:29] And, like, oh, no, this is now, you know, just an engineering challenge.
[40:32] And we're, like, in the last mile of this.
[40:34] And, like, it's basically almost here.
[40:36] And in the meantime, we are scaling on the more traditional front as well.
[40:40] I want to get into the qualitative nature of the scale of the ZK EVM.
[40:45] So with block times and block sizes, those are the two ways that you have throughput.
[40:50] You have how big is your block and how frequently do those come, you know?
[40:54] You know, height times length.
[40:57] So can we talk about what the nature of scaling with a ZK EVM does?
[41:03] Does it help lower block times?
[41:05] Does it just increase block size?
[41:07] I want Onsgar both fast and big blocks.
[41:10] I like my blocks big and fast.
[41:13] It would be great if we could increase the size of blocks.
[41:17] But there is also a very important element of just, like, block times is critically important for trading and finance.
[41:24] Yeah.
[41:24] So how does the ZK EVM impact both of these variables?
[41:28] Right.
[41:28] So to answer that question directly, ZK EVM, indeed, it's not a panacea.
[41:32] It specifically addresses the throughput level.
[41:35] So it gives us much, much, much bigger blocks in the same kind of time constraints.
[41:39] It's even, to be fully transparent, it is a small extra strain on the timing just because you have one extra step, right?
[41:47] You have to have this proving step that's in between block creation and block verification.
[41:51] You have to have proving.
[41:52] But that's a minor constraint.
[41:56] But it in itself does not give us lower latency.
[42:01] And this is why when you said at the top, like, it's the biggest ever change, I was actually tempted to say, well, to me, that's true on the execution side of the blockchain, right?
[42:10] But, like, same as with Bitcoin, how we said there's the consensus mechanism, proof of work in that case, in our case, proof of stake.
[42:15] And then there's the actual processing of the blocks, Bitcoin transaction, Ethereum transactions, that kind of thing.
[42:20] And for the actual execution, for the transaction bits, the ZK EVM and the related changes really are the major story for the next, you know, five years.
[42:31] And we, in parallel, are also, like, now putting together this really, really exciting roadmap on the consensus layer side.
[42:39] And, like, the latency, that's all a consensus layer story, right?
[42:44] Because that's where basically the heartbeat of the blockchain is determined.
[42:48] And so we have this separate process.
[42:52] And you should probably, you know, this is maybe setting us up for a separate podcast episode.
[42:56] You should bring someone on that's specifically focusing on that type of work at the EF and or the broad ecosystem.
[43:02] Because I think we have this really exciting roadmap there that's getting us to a much faster finality.
[43:08] So right now, finality in Ethereum takes two epochs, that's 64 slots, on average, two and a half epochs, actually, even.
[43:16] So it's, like, long amount of time.
[43:18] And we're bringing this down all the way to basically single-slot finality, two-slot finality.
[43:23] Like, it's going to come down, like, orders of magnitude.
[43:26] So that's super exciting.
[43:27] And then even within a single slot, instead of 12 seconds, we have a story there that's going to gradually get us down from 12 seconds to, I don't know, eight, six, four, much, much, much faster.
[43:39] And then there's separate work streams around, can you get even faster inclusion guarantees, right?
[43:44] Like, so that's the heartbeat at which the chain actually progresses.
[43:47] And you get guarantees about that's the result of your transaction.
[43:51] But can you maybe get, in principle, like, speed of light, you know, like, just round-trip time confirmation that your transaction will be included, right?
[43:59] Like, ideally, I want to click a button.
[44:00] And before I can even, like, you know, within the 100 milliseconds it even takes me to realize something happened, boom, I have the confirmation, like, my trade will be included.
[44:09] And then within, like, say, four seconds, I know at which price, right?
[44:11] Like, I think that's the world we ideally want to be in.
[44:14] And we have a really, really exciting roadmap there as well, but it is a separate roadmap from ZKEVM.
[44:18] Okay, understood, understood.
[44:20] So the ZKEVM massively increases block sizes.
[44:23] I don't know if you can put numbers around that.
[44:25] And then it adds a marginal increase in block times.
[44:28] Can that block speed come down in the future?
[44:32] Or what does it take for block times to get faster?
[44:34] And is that something that we are aspiring to in the roadmap?
[44:37] Yeah, that's what I was talking about.
[44:39] Like, we are aspiring to that.
[44:41] That's not just aspiring.
[44:43] That seems so indeterminate optimism.
[44:45] We actually have a plan.
[44:46] And that will come down.
[44:48] It will come down as early as towards the end of this year.
[44:51] That's not quite certain yet.
[44:52] But basically, like, we're starting to make this a priority as well.
[44:54] And it will rapidly then become a major priority.
[44:56] I see.
[44:57] So maybe the part that I wasn't sure of is, like, maybe the block speeds don't necessarily come down.
[45:04] But transaction assurances come down very, very fast.
[45:09] And you're kind of saying, well, that's what people want anyways.
[45:11] Is that correct?
[45:11] Well, it's basically, you have three things.
[45:13] You have the time to inclusion confirmation.
[45:15] You have the actual time to the next block.
[45:17] And you have the time to finality.
[45:18] All three of these will come down.
[45:19] The heartbeat of the chain, the time to next block, will actually be the one that's only going to come down maybe by a factor of three, something like that, from 12 seconds maybe to four seconds eventually.
[45:28] Maybe we can go lower, but I don't necessarily want to promise this.
[45:31] I think the other two are actually the more exciting ones.
[45:33] Finality will come down.
[45:35] Massively.
[45:35] And time to inclusion, that's a bit more of an exploratory process still, but that also will come down massively.
[45:43] So I think basically, like, yeah, but block times as well will come down.
[45:47] But none of this will be through ZKVM, although, of course, it will be part of an integrated system.
[45:51] Right.
[45:52] Okay.
[45:52] Understood.
[45:53] Okay, so you're saying there's a variety of ways in which Ethereum speeds up broadly.
[45:58] And then there's, like, zooming into what speeding up means, you know, has nuances, which you just went into.
[46:04] And as, at least when it comes from a user experience perspective, we have ways of providing essentially instant speeds from the perspective of a user.
[46:13] Right.
[46:15] Let's talk about the rollout plan for the ZK EVM.
[46:19] We are in a phase of Ethereum where there is no ZK EVM.
[46:23] In the future, we will be a phase of Ethereum where it is all ZK EVM, but it is not an acute moment, as I understand it.
[46:30] How do we go from A to B?
[46:31] What does that roadmap look like?
[46:33] Of course, because this is, like, a multi-year process.
[46:37] It's as typical.
[46:38] There's, like, very concrete steps as, say, for the next 12 months.
[46:42] And then as you go further into the future, I can more point out that's the current plan.
[46:46] These are maybe the open question.
[46:47] These are the directions, right?
[46:48] So that's how these things always work.
[46:50] The interesting thing, as I said, top of a podcast, is that it's not just a one-time hard fork.
[46:57] There will be a one-time hard fork, and that is about the eventual switch from what will come first, which is optional ZK EVMs for those nodes in the Ethereum network that want to consume proofs instead of re-executing.
[47:10] Then at some point, there will be this moment in time where we say, okay, now Ethereum just runs on proofs.
[47:17] Of course, you can still run a node optionally in re-execution mode if you want to, but by default, like, the network now guarantees that there will always be proofs, basically.
[47:26] And then from this point where the switch to mandatory proofs is, is when you really get the scaling gains.
[47:32] Because before then, you're basically not yet mandating that anyone, right?
[47:35] So, like, you're still allowed to run a full re-execution node.
[47:38] You're allowed to be slow, and the network will hear you.
[47:41] Exactly.
[47:42] And after that, it's like, okay, if you want to be a re-execution node, that's a special purpose role now.
[47:47] That requires special purpose hardware.
[47:48] Of course, internally, it is a big project.
[47:51] Like, how do we make sure that if we run at much faster speeds that you can still run an RPC node in a performant way, right?
[47:58] So, like, this is a separate work stream that we're working on.
[48:00] But in terms of, like, the typical validator even and the typical full node out there that's not even a validator, those people basically, by default, will all at that point then switch over to ZK.
[48:11] Now, again, as I was saying, before then is this phase of optional proofs.
[48:15] So, that has not started yet.
[48:16] Like, right now, we're in the proof of concept phase.
[48:19] So, like, I think Justin presented in Buenos Aires this proof of concept of, hey, see, my validator canon principle already run on ZK.
[48:26] But that's not yet, like, if you're a validator, like, you can't use this yet today, right?
[48:31] But the idea is that very soon, so meaning within, say, the next 12 months or so, we are starting to put this out there in a early production-ready state, where the idea is that we will, of course, we will give very quick guidance of, like, this is the specific nuanced level of confidence we have yet in the security of the system, all these kind of things, right?
[49:01] And, for example, at that point, we could not yet have the majority of the network run on this yet, right?
[49:05] Because, like, if there is some bug with it or something, right, you very much still want to have the backbone of all the major validators run on this.
[49:12] But if you are just a full node, just for hobby purposes, or maybe you're a validator on a very weak machine, you might be tempted to just, at that point, transition over.
[49:20] So, that will be the first step.
[49:21] And then one thing we haven't really touched on yet is that, like, well, I guess a little bit, is that there's actually quite a few technical requirements that we need to hit before we can move the bulk of validators over.
[49:36] And I can briefly go over those.
[49:37] So, one we already touched on, for example, is the block in blobs, which will come at some point where we basically say, look, we now put the block into the data, so there's also the sampling aspect to it.
[49:49] If you are a re-execution node, you still download all of it.
[49:52] But if you now are a zk node, you can start only sampling it, right?
[49:55] But this will come after the initial optional proofs rollout.
[49:58] So, before then, a validator basically has to download the proof, but also has to download the full block still.
[50:03] So, it means they don't yet gain any bandwidth benefits.
[50:07] They only get the IO and the compute benefits.
[50:14] So, basically, like, we have the block in blobs that will have to come.
[50:16] We have to have, in general, networking improvements that are in the works.
[50:21] We have repricings, meaning we have to actually make sure that the parts of the Ethereum chain that are especially hard to zk verify, we make a bit more expensive.
[50:30] We basically rebalance the cost.
[50:32] And then, the most important technical dependency for the mandatory proofs, the full transition, basically, is actually, it's related to the statusness element.
[50:44] And that's specifically that we need to transition the Ethereum state tree over to a new format.
[50:51] Like, long-term listeners might be familiar with this, like, elusive Verkle tree idea, right?
[50:56] And so, Verkle trees were this early Ethereum idea of, like, hey, we can currently have a Merkle tree, so, like, any account in Ethereum is part of this huge tree structure, and every block, the entire tree is updated.
[51:08] And, you know, at the roots, you have your balance, and you have your, you know, all these individual elements about your account.
[51:14] The original idea was that transition is over to a more efficient form, and it's called Verkle trees.
[51:20] And that was the unfortunate fate that Verkle trees had, is that they were just never really necessary.
[51:26] They were always, like, one of those nice-to-have features.
[51:28] Back then, back then, we were not quite sure, like, how aggressive do we want to scale?
[51:32] How quickly will state growth become a problem?
[51:34] There was some worlds in which it would have been a more urgent topic, but because we never went down those routes, it was always, like, right beyond the edge of urgent enough to ever do.
[51:43] So, we never ended up shipping Verkle trees.
[51:45] But the nice thing is, we now already have a lot of prior work, and now we can actually go directly to the next generation of cryptographic structures here.
[51:55] And so, instead of a Verkle tree, we're going to something that's basically called a unified binary tree.
[52:01] It's somewhat similar.
[52:03] The main difference is that it has a very different kind of, like, instead of, like, a Verkle tree is a very wide tree, a binary tree is a very narrow tree.
[52:11] And the main, I guess, simple set, the main difference is that the binary tree uses a post-quantum secure hash function that is also very efficient to prove.
[52:22] So, it's already basically, like, fitting into this, like, future world that Ethereum is going to, whereas the Verkle trees were basically the standalone piece that doesn't quite fit.
[52:30] But the nice thing is, we have a lot of prior expertise.
[52:33] We have Guillaume, who has been the champion of Verkle trees, and he's been frustrated to no end that we never ended up shipping it.
[52:39] And now, his time has come.
[52:41] So, like, he's been very excited.
[52:42] He's now working towards this binary tree upgrade behind the scenes already, and he's doing an amazing job there with his team.
[52:47] And so, actually, over the next two years, I would say the biggest kind of individual story that we'll have in Ethereum will be this upgrade to binary trees.
[52:59] So, that will probably, over the coming months, start to become a bigger and bigger topic.
[53:03] People will start hearing about it.
[53:05] And that will then enable very efficient stateless operations or partially stateless operations for nodes.
[53:10] So, to recap, basically, starting a year or so from now, we will roll out optional proofs.
[53:18] Those optional proofs will initially only be immediately effective for compressing computation and helping somewhat with IO load, but you still have to run in stateful node.
[53:29] And then we will, bit by bit, start bringing these pieces into the protocol that unlock the full potential of ZKEVM and, in parallel, keep hardening the ZKEVM security properties so that by the time we are running out of conventional scaling means, which is why all of this is so beautiful.
[53:48] Like, we basically have exactly like three years of scaling, or like two and a half more years of scaling ahead of us, of traditional scaling.
[53:54] And at that point, we will be ready to just seamlessly move over to ZKEVM.
[53:57] So, one year from now, optional proofs.
[54:00] Two and a half years from now-ish, plus minus, this full transition to mandatory proofs.
[54:05] And then we'll have all the pieces ready to then immediately keep scaling based on ZKEVMs after that.
[54:10] So, that's the, like, the fallout.
[54:13] Right.
[54:14] So, as I understand it, the way that it happens is that in a year, we will introduce optional proofs.
[54:21] The Ethereum enthusiasts of the world who just, you know, love Ethereum, tinker with Ethereum, run nodes for Ethereum out of just pure passion, will start to do these optional ZKEVM proofs.
[54:33] They will be the pioneers of the transition of Ethereum to be, you know, a classical blockchain transitioning into a ZK blockchain.
[54:40] And that will give, you know, Ethereum researchers like you, the EF, a lot of data of what it looks like to be in production because of these enthusiasts that are running this optionally because they just, you know, love Ethereum so much.
[54:53] That will give you guys the information you need to do the prerequisite upgrades that are needed to actually get a full mandatory ZKEVM fork.
[55:03] And as you alluded to, it will also give us just insight into, you know, in production use of the ZKEVM.
[55:10] Maybe there are bugs.
[55:12] If there are bugs, we need to find them before we make them mandatory.
[55:14] And so, you know, all the different clients will have their own version of the ZKEVM and we'll be stress testing all of those by using them into production.
[55:22] Basically, there's a whole era of demo Ethereum ZKEVM.
[55:27] And that will take, I think you said, you know, somewhere two to three years.
[55:31] As we run out of classical scaling, that will have, we will have the hardened data and the information.
[55:36] We will do the prerequisite work to unlock mandatory ZKEVM.
[55:40] Around, you know, two and a half, three years from now, the mandatory ZKEVM hard fork will happen.
[55:47] And then Ethereum will make the transition to this is now a ZKEVM blockchain.
[55:51] The story doesn't end there, though.
[55:53] What happens after the mandatory ZKEVM fork?
[55:57] How does the story continue beyond that point?
[55:59] And just by the way, to clarify a little bit for people that maybe think, oh, we are now gung-ho starting to release optional proofs for anyone who wants to be like a experimental, you know, like guinea pig here.
[56:08] I think when we are ready to start releasing this, like there will be very explicit guidance around like what is this for?
[56:19] Like what kind of production grade readiness does this have for which use cases?
[56:23] I think it's more, you can imagine more like it's about like how many nines after the comma, right?
[56:28] Like Ethereum main, it must never go down, right?
[56:30] Like we have 100% uptime and we're not willing to risk this.
[56:34] So we are basically willing to take extra precaution there.
[56:38] But importantly, if you're, for example, at some point running a ZKEValidator and you actually daze a bug or something, right?
[56:44] The worst that happens, like no one will get slashed, right?
[56:47] Like what happens is just you're briefly kicked off the chain and then you're automatically flipping over back to normal re-execution mode.
[56:54] And then worst case, if we're already in this partial status world, you might have to first re-sync some of the state, right?
[56:59] So worst case, you're offline for a couple hours and then you're back online, back on the chain.
[57:04] So none of this, we do it very responsibly, just because, you know, just to clarify this.
[57:08] On brand.
[57:08] But yeah, so, and basically I think the way that these, again, absolutely amazing ecosystem ZKE teams are talking about this.
[57:15] I think last year was all about, I would say it was the year of performance, getting to real-time ZKEVM.
[57:20] This year is the year of security, getting to like absolutely hardened.
[57:24] And there's also like this bit of security measure, right?
[57:27] Like getting to a level where we are very confident in the security level.
[57:30] Then next year, I think will be the year of productionizing the ZKEVMs.
[57:36] And then the year after will be the year of like transition to mandatory.
[57:39] So like that's basically like the performance, security, production, and then like full transition.
[57:45] That's how I would think about it is like one year at a time.
[57:47] In terms of what comes after the transition, well, it's just, I think, and that's why I was saying earlier, like with the further you go out, the more unknown unknowns there are.
[57:56] It's just about saying at that point, we will have all of the ingredients.
[57:59] Like, you know, we have the state partial statusness, we have the block and blobs, and we have the ZKEVM to take advantage for scaling.
[58:06] But we don't expect that once we get closer, that it's like a one-time switch and now we can run it a thousand times faster.
[58:12] And instead, we basically like right now, conservatively, quote unquote, are projecting this three times per year, because we expect that there will be individual remaining challenges we have to address, right?
[58:23] Maybe we have to restructure the way nodes sync, or maybe you have to restructure the way RPC nodes, again, operate.
[58:28] So you can, you're confident that the chain is still usable at higher rates, right?
[58:32] So this is just expressing that while we have the main architectural ingredients, there will still be a lot of like detailed work.
[58:39] And so we expect, instead of making use of it all at once, it's going to be this continuous process.
[58:44] And again, if you, the nice thing about this rough 3x number is if you just say, look, every two years you get a rough 10x, 9x, 10x.
[58:51] So basically, we're thinking we have like a path for maybe five or six years of this.
[58:56] So six years at 10x every two years means a thousandx.
[59:00] So basically, the first three years of that we get traditionally, then the next three years, so the ZKVM, so in six years, roughly a thousandx of where we started last year.
[59:10] That's, I think, the, again, is this guaranteed yet?
[59:14] No, we don't yet, we don't yet have, we just, we think we see a path.
[59:17] We think we see a path.
[59:18] That's our goal.
[59:19] And then, of course, beyond that, you could, if you want to be like more in sci-fi world, like now you can think about native rollups.
[59:26] So maybe the way we then keep scaling beyond that is not through just the single chain.
[59:30] You know, maybe then we're back to this kind of sharding type setup of multiple chains, synchronously composed.
[59:38] Yeah, we'll have to see.
[59:39] But that's the plan.
[59:41] What if you could trade gold, forex, and global markets with the same tools and speed that you use for crypto?
[59:47] That's exactly what BitGet TradFi unlocks.
[59:50] After strong beta demand, including over $100 million in single-day gold trading volume, BitGet TradFi is now live for all users.
[59:58] Inside of your existing BitGet account, you can trade 79 instruments across forex, precious metals, indices, and commodities, all settled directly in USDT.
[60:06] No platform switching and no fiat conversions.
[60:08] This is BitGet's universal exchange vision in action.
[60:12] Crypto and traditional finance side by side.
[60:14] You get deep liquidity, low slippage, and leverage up to 500x, letting you apply crypto strategies to macro markets.
[60:21] New to TradFi?
[60:21] Start with gold.
[60:22] The gold-USD pair is liquid, macro-driven, and a familiar natural bridge between crypto and traditional markets.
[60:28] Try trading gold on BitGet now at bitget.com.
[60:31] Click the link in the show notes for more information.
[60:33] This is not financial advice.
[60:34] Few people in crypto put real skin in the game when they make public top or bottom calls.
[60:39] The DeFi Report is one of them.
[60:41] The week before the October 10th flash crash, Michael from The DeFi Report emailed his entire newsletter saying he's going aggressively risk-off and sold the majority of his book from crypto into cash.
[60:51] This is when ETH was about $4,000 and Bitcoin was $110.
[60:54] Michael runs The DeFi Report, an industry-leading research platform built on data, cycle awareness, risk management, transparency, and most importantly, skin in the game.
[61:03] We like Michael at Bankless.
[61:04] We like his analysis, and that's why you hear him on the Bankless podcast about once a month.
[61:08] And The DeFi Report is giving Bankless listeners one free month of access to The DeFi Report.
[61:12] So if you're looking for some sharp, data-driven analysis to make better informed decisions around your portfolio, you can learn why and how Michael called the top and what he's doing next, all in The DeFi Report Pro.
[61:22] Check it out.
[61:23] There is a link in the show notes.
[61:24] Ansgar, as I understand it, client diversity is a big topic here.
[61:29] Why is client diversity relevant to the ZKEVM, and how does the ZKEVM impact it?
[61:34] So, I mean, of course, I think people will be familiar why client diversity is so core to Ethereum and to Ethereum's kind of 100% uptime, right?
[61:41] Like, there's the redundancy factor you get from client diversity.
[61:46] And so the reason why this is relevant is just that, like, the nature of clients, the nature of client diversity changes in this world.
[61:53] And that is because, again, if we think back to how I explained how there's, like, this basically most likely RISC-V kind of intermediate target for ZKEVM, and then you basically just run a, of course, heavily modified, but basically like a traditional execution layer client that gets compiled to RISC-VM.
[62:10] And then you take one of those new ZKEVM proving systems that then take the RISC-VM code and prove execution over it, right?
[62:18] So what that means is now basically the Ethereum execution layout nodes live inside of the ZKEVM proofs, right?
[62:25] Which is, of course, conceptually, like, very different from what that used to be before.
[62:28] And so what it means is that now the actual node architecture is actually quite interesting.
[62:32] You basically, you run, and that is a little bit still TBD.
[62:35] Like, it might be that you're still running this explicit split of two clients, like the consensus layer client and the execution client, but the execution client's role is very different now.
[62:42] It basically just verifies the proofs, the one that you run locally, right?
[62:46] It just verifies the proofs and does some maybe, like, mempool networking, that kind of stuff, state management, but inside of the proof lives the ZKEVM program that was also derived from an execution layer client.
[63:02] So if you think about the roles of clients now, basically it means that the main question is, like, what about the diversity within those proofs, right?
[63:12] Because the outer system we are familiar with, but what about the diversity within those proofs?
[63:18] And so the nice thing is that, in principle, you kind of, you get a very comparable, very parallel type of mapping where you can just, you know, you don't just take a single execution client and compile it into RISC-V, you take multiple.
[63:33] So, you know, you basically take kind of, you know, the existing ones you know, or, like, also there's a few ones that will be specially written for that use case.
[63:42] So you compile all of those, and then to make sure that the redundancy is full stack, not just the first half of the stack, you also have multiple of these proving systems that take RISC-V, because, of course, there could also be a bug in that part of the stack, right?
[63:54] Like, that take the RISC-V and prove over it.
[63:56] So you say you have, like, as an example, five of each, right?
[63:59] You have five execution layers that can be compiled into this RISC-V, and then you have five different proving systems.
[64:04] And what you can do is you can basically build pairs of those.
[64:08] So you can say, and Justin has this really nice idea where you can even, you could, in principle, even, like, say, performance match them.
[64:13] So maybe the fastest execution client is paired with the slowest proving system.
[64:17] So you basically, so the pairs kind of balance each other out.
[64:19] But that's just an idea.
[64:22] But basically, the point is you then have these combinations of, like, okay, this execution client with this proving system.
[64:29] And then in the end, you basically, you're, again, in this example of five, you'd be in a world, again, where you have, like, five different types of proofs that could all, and they're all kind of redundant.
[64:38] They all have different, you know, they're full stack different from each other.
[64:41] And the generally novel thing here is that today you run one execution client, right?
[64:48] Like, there's multiple, of course, and there's multiple consensus their client, but you choose one, one of each.
[64:52] And in this new world, what you can do is you can just verify multiple proofs.
[64:57] So, for example, there's this idea, and again, just to use example numbers, but they seem roughly ballpark, right?
[65:03] You could have a system where you say, I only accept a block if I saw at least three different valid proofs for it.
[65:09] So, I know that there are these five different ones, and I have to have seen at least three of them, otherwise I don't accept the proof, accept the block.
[65:16] And so, that actually gives you better redundancy because it's kind of almost as if every Ethereum node today would run three different client setups and would basically only accept blocks if they all agree, which, of course, gives you much better properties.
[65:28] Then right now, we only have the redundancy across nodes, not within a node.
[65:32] So, it's actually, it's a better story, but it's also one where you actually have to be intentional so that you don't accidentally collapse any layer of the stack.
[65:38] And as just a side note, there is this experimental idea, and of course, in the age of AI, all the timelines collapse.
[65:44] So, who knows, you know, like maybe that's actually even short-term viable, but this experimental idea of a fully formally verified client.
[65:53] And you could imagine, right, like an EVM implementation in RISC-V that is fully formally verified to be correct.
[65:58] In that world, that could basically then, you would no longer need redundancy at that layer of the stack.
[66:03] But again, this is, as I said, like the further out items have some uncertainty.
[66:07] This is like one of those theoretical out there approaches, but that, of course, would be also really nice to have.
[66:14] And I think formal verification in the age of AI will become a much bigger deal anyway, so this might be a really nice synergy.
[66:20] Yeah.
[66:21] As I understand it, the clients are where all of the risk is with the ZKEVM and where we have to be, have like an extreme level of caution with the transition from a classical blockchain to a ZK blockchain.
[66:35] And like if something is going to go wrong, it's going to go wrong at the client level.
[66:40] I mean, I suppose that's always where it would go wrong.
[66:42] But when we, you know, we have, you know, Ethereum has over a decade of uptime because of client diversity, because of how hardened these clients are.
[66:51] And we are kind of resetting that to kind of go back to, you know, zero Lindy with the ZKEVM.
[66:59] You know, we have some properties that will be carried over, but nonetheless, there will, it's, it's risky in the sense that like we have all this great hardened infrastructure and we're kind of rebuilding it to be ZK.
[67:11] And so we have to have this like extra levels of redundancy, as you said, like three proofs, three correct proofs to make sure that, you know, not just two proofs, because two proofs might have the same bug.
[67:22] So we might prove the same bug twice.
[67:24] So three things like this.
[67:26] And so, you know, what's your level of fear about this part of the transition for Ethereum from like the classical blockchain, which is so hard and 100% uptime to go where we go here.
[67:39] Like how scary is this?
[67:42] Oh, it's a, it's a really good question, right?
[67:43] Because I think the promise here is so huge that we're all very, very excited about this, but it is also generally like a huge, a very, very big challenge.
[67:51] And this is why I think it's not at all natural that we are even doing this two-step rollout with optional proofs and then the mandatory proofs.
[67:57] In principle, we could switch over at the end of this year, right?
[68:00] And we, we already plan with this extra 18 months period specifically because of that, like that level of certainty that, that we want and that, that we project, like that will just take some more time.
[68:11] Again, it also gives us the extra time to roll out these other dependencies to really make use of CK proofs.
[68:15] So it's actually quite synergistic, but, but still, right?
[68:17] Like this extra 18 months delay is specifically for that reason.
[68:20] And to be clear, like we would always be responsible with this.
[68:24] So like, if it turns out 18 months are not enough, of course we would like delay this full transition to mandatory proofs.
[68:29] Maybe we even find some more gains we can get on the classical scaling side until then, right?
[68:34] So like maybe it wouldn't even matter, but basically we would always wait until we're like really, really confident.
[68:39] And it's, it's not in principle harder, but it's just, as you said, right?
[68:44] Like it's, it's, it's a bit of a reset.
[68:45] So like a lot of say our internal expertise, both inside of the EF and across the client teams around security work, testing work.
[68:52] A lot of this is currently actively being restructured for this very new domain, for this very new type of operations with CK, understanding like what even are the weak points here?
[69:02] Like also say on the cryptography side, like how we have, we have absolutely world-class cryptographers inside of the Ethereum Foundation and, and, and, and in the ecosystem.
[69:10] And, and they are like very thoroughly, like really turning around every single stone here in this, in this overall like stack and really making, making us understand like what are the critical points here?
[69:19] And, and again, like how far are we from, from being, being willing to, to actually trust this?
[69:26] And, and it's actually, so for example, just to take, take, take a related example.
[69:29] I'm not sure if you already had maybe an episode on, on post-quantum, but that's also a big topic on Ethereum.
[69:34] We will soon, yeah.
[69:35] Yes, mostly unrelated, but of course, of course there's, there's synergies here and, and it has a similar nature where, and I talked about the binary trees and part of the binary trees is this choice of hash function that you need in the tree.
[69:46] And, and there, for example, we also like currently not blocked, but like the, the, the, the longest piece of the timeline there is us talking with our cryptographers.
[69:55] We have a candidate, like a set of kind of a family of candidate hash functions, but getting to this point where we're saying, look, they are actually robust enough.
[70:05] They have been around long enough that we actually trust that they are secure, right?
[70:08] Like especially something like hash functions that's so fiddly, you can't really prove security.
[70:11] You're just, it's, it's basically like a lindiness to it, right?
[70:14] Like how long has it been around?
[70:16] How many people have tried to find vulnerabilities?
[70:17] Has there been anything found, right?
[70:19] This kind of thing.
[70:19] And so some of these things you just can't accelerate, right?
[70:22] Like how many years of academics having looked into this has there been, right?
[70:27] That's just like a hard constraint.
[70:28] And so both in this post-quantum, but also then binary trees, we're also using for making use of ZKEVMs.
[70:34] It's not directly ZKEVMs, but making use of them.
[70:36] There's just some, some elements of the timeline there that are dictated by the security needs that we have.
[70:42] And, and we just can't cut corners.
[70:43] So it's a big concern, but I think we are very responsible about it.
[70:47] Yeah.
[70:47] Yeah.
[70:47] Yeah.
[70:48] Which is why it's taking, you know, not a short amount of time.
[70:51] So just to maybe conclude this podcast, the timeline, it is now at the start of 2026.
[70:57] By the time we hit 2030 is a good guess for when we think we will have the full power, the full properties of the ZKEVM.
[71:09] You're nodding your head.
[71:10] Does that sound right?
[71:10] That sounds right.
[71:11] And I think we will be still probably in the process of making full use of it for scaling.
[71:15] So we will be, hopefully 2030 will be another 3X year, maybe more than 3X because we have AI and the hard fork timelines are compressing.
[71:22] But basically another 3X year in 2031 will look like another 3X year.
[71:26] So we will be on this continuous scaling path, but already squarely in the ZKEVM backed side of that scaling path.
[71:34] Right, right.
[71:34] I guess one point you made earlier, and I guess it's worth reemphasizing here, is we are, the aspiration of Ethereum is to do a 3X scaling increase every single year, not just for the next three years, next three years for classical scaling.
[71:48] And then the next three years after that for ZKEVM scaling.
[71:51] So, you know, while I am excited about the ZKEVM and I think it's incredible and why I want to like rally the Ethereum community around it, acutely there won't be a ZKEVM moment as felt by the transactors, users of Ethereum, because we are doing a 3X scaling per year for the next six years.
[72:14] First with classical, then with ZKEVM, and so, you know, while the merge, you know, acutely transitioned us from proof of work to proof of stake, EIP1559, acutely transitioned us from, you know, to have the burn and better transaction UX.
[72:27] And like same thing with 4844 is an acute transition.
[72:30] This won't be that because we are scaling anyways.
[72:34] But nonetheless, I think it is important to know that like only Ethereum will actually be able to access, you know, the final, you know, years three through six of scaling in that capacity because this is Ethereum's Manhattan project.
[72:50] Like we said, only Ethereum has been working on this.
[72:53] It's been working on this since Genesis.
[72:56] And while Ethereum makes this transition from a classical blockchain to a ZKEVM blockchain, it will be leaving every other blockchain behind in the previous classical era.
[73:06] And so maybe that's why I'm so excited about it is like Ethereum is making the generational leap to the next gen blockchain and no other blockchain will have these properties that we've been discussing about on this podcast.
[73:19] Well, and I think this is what I said earlier, like it's not just that, like it's not an accident that you won't notice this transition.
[73:28] Like it's actually by design, like we're trying, we're like, I think in this moment in time, we're really trying to balance this, continue the strength of Ethereum of being able to make these like leaps, these paradigm jumps that I think like other projects really struggle to be able to follow.
[73:42] I think, again, that's why we'll also just naturally have the post-quantum properties.
[73:46] I think many chains will actually like struggle quite a bit with actually getting there.
[73:50] And at the same time, realize that now we're no longer in the sandbox mode.
[73:56] We can't just like say, I just wait, just wait for three more years.
[73:59] Like how, you know, like don't be so impatient.
[74:01] Like, no, no, no.
[74:01] I mean, people are coming on chain agents, AI is like coming on chain like today, right?
[74:07] So like, I think it's important that we basically just like, we are a continuously scaling blockchain.
[74:12] And it's our responsibility to under the hood, make that happen and like use whatever, like both traditional and magical future ZK means necessary to make that happen.
[74:21] And I will say, because you said like no one else will be able to do that.
[74:25] I think, I actually think it's one of those areas where there's, again, natural synergy between Ethereum and like the EVM L2 ecosystem.
[74:34] I think one thing that, for example, we didn't talk about at all, but that I'm very excited about is that like, again, similar to how the initial jump to non-real-time ZKVM came mostly driven by the L2s.
[74:45] I think now that we are driving from the L1 side, this move to real-time ZKVMs, the L2s will also be huge beneficiaries of this because they will also just become the, like, or like, gain the ability of real-time settlement.
[75:01] So that means also say all the like bridging pain across the L2 ecosystem, right?
[75:06] Like, oh, in principle, it takes either I use a mint and burn bridge or it takes like seven days for my asset to move across chains.
[75:12] All of this will disappear, right?
[75:13] I think that it's going to be a few seconds for any asset to move from any L2 to any other, any real-time ZK EVM proven L2 to any other real-time ZK EVM proven L2s through the Ethereum L1 or, of course, into or out of the Ethereum L1.
[75:26] So I think it's yet one of these cases where the fact that if you're part of the Ethereum family, we're like, this is kind of, this is the ecosystem that really has this principled approach to things.
[75:35] You get all of these benefits for free.
[75:38] You're basically, you are on the principled architectural path.
[75:41] And I think that has always been our competitive advantage.
[75:44] And I think while doubling down on the competitive advantage, I think we really are already trying very hard.
[75:50] I think we have to keep trying even harder to close where maybe we've had the competitive disadvantage, which is I think that Ethereum in the past has sometimes been a bit too much in this pure research mode and like maybe discounting the type of activity that already existed and saying, ah, that's just sandbox, whatever.
[76:05] Like the real world adoption will come later and then we'll start focusing on it.
[76:09] Real world adoption is clearly here.
[76:11] And so finding the right balance, I think, is the ongoing challenge.
[76:14] It's what, for example, Tomas and Chauwei in their time at the Ethereum Foundation have like really put a lot of focus on.
[76:20] And I think that's how I would like narrate the future of Ethereum, both the Manhattan Project and the short-term focus and ownership of the protocol as a useful thing today.
[76:30] One theme that I've picked up on a handful of your answers throughout this conversation on SCAR is that there seems to be a significant number of second-order positive effects of the ZKEVM that are not related directly to the main quest line of the ZKEVM, which is just straight, you know, layer one scaling, but solves a bunch of second-order problems, you know, layer two scalability and composability being the one that you just said.
[76:56] How big is that second-order effect?
[76:59] It's like, am I correctly identifying that it's actually like somewhat large in the positive second-order effect number?
[77:05] Yeah, I mean, I think there's the immediate second-order, like the, as you said, like the things that, like just the benefits to the broader EVM ecosystem, especially EVML2 ecosystem, because again, I guess maybe I didn't mention this so much.
[77:19] Like, I think, I think it's much easier to adopt, to benefit from this technology for L2s, for EVML2s, whereas like other EVML1s, I think, while I think that's actually, it's also very exciting for them, I do think, basically, you'd have to re-architect your entire chain, right?
[77:39] Similar to how I was saying, like the Ethereum L1, it's, the ZKVM is the core piece, but there's like many elements to it, right?
[77:44] Whereas, because the L2s already have this architecture where they are just like naturally settling on the L1, they just have to compress the timeline, like the settling time.
[77:53] Like, for them, it's like a, it's almost like a trivial upgrade to follow us to this world.
[77:58] And like, so I think, I really think there's the unique synergy for the Ethereum L1 and then the Ethereum EVML2s.
[78:03] I think longer term, if I'm talking beyond blockchains here for a second, I think we've already seen how in the world outside of crypto, we are starting to see this like second generation of cryptography really impact and it become very impactful.
[78:17] It took a while, it took a couple of years for people to start taking it seriously.
[78:22] And so I think you can start to see it with all kinds of things like Microsoft is, you know, doing things like a lot of governments are doing, like, I know, ZKID type of systems.
[78:32] You're starting to really see use cases that go beyond just blockchains.
[78:36] Blockchains are like the most valuable, so that's why we always see the technology there.
[78:41] But you can imagine a world, and especially once you have this real-time element unlocked, you can imagine a world where like, I know, just to, you know, to be futuristic here, like AI agents might use real-time ZK proofs to make provable statements for trustless interactions with each other, right?
[78:57] Like some of that might be on-chain for like, you know, for direct and asset-backed interactions, but some other things might just be literally just, ah, I'm just proving that I have access to this data and this data has this structure and that I, you know, all these kinds of statements.
[79:09] You can just turn trivially real-time proof that you just couldn't before.
[79:13] So I think that's a five-year down the road maybe kind of thing, but five to ten years, but that will come, and that I think will be really exciting.
[79:18] And then, for example, I don't know if you've seen this, like more and more countries are starting to introduce, I don't know, social media bans for like minors and that kind of stuff.
[79:30] And like usually that's implemented in a super dumb way.
[79:31] You have to like just, they use a service, you have to upload your ID to the service, right?
[79:35] And if we can replace that with like a ZK ID system where you really don't leak anything other than I own an ID and my birth date is above this level, this threshold, like obviously that's a much preferable world.
[79:46] So I think we are currently like, I think blockchains and especially the Ethereum ecosystem is currently like funding this massive leap of the cryptography toolkit that we have.
[79:56] And with some delay, five to ten years delay, it will also hit the non-blockchain space, and I think it will be super impactful.
[80:02] Yeah, yeah, yeah.
[80:03] One, you know, idea I've had is that, you know, Ethereum and all the research that we have invested in over the years, hopefully is one big contributing factor to like kind of restoring the brand of crypto by helping the world overcome some like generational challenges as you've, as you correctly identify, you know, you know, crypto doesn't really have the best brand at this present moment.
[80:27] Hopefully, with some of these, you know, sci-fi tech advancements, this Manhattan project that Ethereum has been working on, we don't just, you know, improve the nature of our own blockchains, but we improve the nature of the world around us.
[80:40] And the second order effects upon Ethereum as a brand, as an ecosystem, ETH price is benefited downstream of all of that.
[80:49] Ansgar, this has been a super educational episode.
[80:52] I really appreciate you coming on here and giving me and the Bankless Nation the time about the ZKEVM.
[80:56] I think, you know, broadly, the crypto industry is looking for reasons to get bullish about something.
[81:02] I think this is a very valid thing to be excited about and to be bullish on.
[81:06] And so I'm trying to rally the troops around the ZKEVM fork just in mindshare, in education.
[81:12] And I think you've done the job I've hoped we could do here on the episode today.
[81:17] So I thank you for that, sir.
[81:20] Sounds good.
[81:20] And one last caveat, just to repeat this, right?
[81:22] Like, I'm not personally a ZKE expert.
[81:24] I mean, obviously, I'm in the loop on a lot of these things, but I'm more like a broader scaling expert.
[81:29] So this is part of my job.
[81:31] But really, we have absolutely amazing people.
[81:35] So I'm sure I got like some of the minute details a little bit wrong and the people will scream at their monitors.
[81:41] But I hope I got the broader picture roughly right.
[81:44] And I agree.
[81:44] It's very exciting.
[81:45] I think both the execution layer side, the ZKEVM scaling story, and then on the consensus layer, like these next generation upgrades we're planning there.
[81:53] Very, very exciting.
[81:54] I do think we should understand, though, in this moment in time, also, I think we should try to become more and more the boring infrastructure layer.
[82:03] And I think we should really like ready the stage for the applications.
[82:07] And so I'm personally like incredibly excited for like the actual real-world application side of crypto.
[82:13] We're really starting to see this come online.
[82:15] Argentic payments, real-world assets, stablecoin payments, all of this is incredibly exciting.
[82:20] I think it's a great moment to be in crypto.
[82:23] And yeah.
[82:24] And of course, one last shout out there, maybe actually, if anyone listening to this was actually interested, excited by these technical details of everything we talked about, though, and actually wants to help on the infrastructure side, do reach out to me, I don't know, either on a Twitter DM or unskirtetherium.org.
[82:40] We also always, in principle, are hiring if any smart kid out there, like, really would want to join us here on the infrastructure side.
[82:48] It's not the only exciting thing in crypto, but it is still very, very exciting.
[82:51] And please, come join us.
[82:53] We'll make sure your Twitter is in the show notes on YouTube or Twitter or wherever people are listening to this podcast.
[82:59] Ankar, thank you so much.
[83:00] Thank you very much.
[83:02] Bankless Nation, you guys know the deal, crypto is risky.
[83:04] You can lose what you put in, but nonetheless, we are headed into the future.
[83:08] We're going to ZK the future, too, with the help of the ZK EVM.
[83:11] That's not for everyone, but we are glad you're with us on the Bankless Journey.
[83:14] Thanks a lot.
[83:32] Transcription by ESO. Translation by —