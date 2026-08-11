---
channel: "Bankless"
video_id: "lRuaC0JkWhU"
title: 'NEAR’s New Token Model for the AI Economy'
published_at: "2026-08-11"
duration: "52:36"
word_count: 53129
---

# NEAR’s New Token Model for the AI Economy

[00:00] - Bankless Nation, there was a big announcement and evolution in the NIR part of crypto.
[00:07] The NIR token has gotten a little bit of an upgrade.
[00:10] There's now a more formal integration between the NIR AI cloud and the NIR token.
[00:16] So you can now pay for inference on the NIR AI cloud by staking NIR.
[00:21] So stake NIR, receive free inference for yourself or your agent.
[00:25] Here to help me learn a little bit more about how this all works is Ilya, co-founder of NIR and co-author of the famous Transformer white paper.
[00:32] Ilya, welcome back to Bankless. - Thanks for having me.
[00:35] Yeah, very excited to talk about it. - It seems like one of the larger upgrades to the NIR token that I've seen in a while, in order to really understand it, I think we kind of need to just start from the basement with the NIR AI, like part of NIR.
[00:49] NIR itself seems to be like a collection of things.
[00:53] You have like the actual NIR blockchain, you have the confidential Intense and then the NIR AI cloud, like one of these pockets.
[01:02] How does the NIR AI cloud work?
[01:05] What actually is it?
[01:06] How does it work?
[01:07] Can you like paint a picture for me? - For sure, yeah.
[01:09] So I think of NIR less as a collection and more as a vertically integrated stack.
[01:13] So each piece actually builds on top of each other.
[01:16] Intense is obviously using all the blockchain tech.
[01:19] There's a kind of our core cryptography primitives at the core.
[01:24] And so NIR AI actually builds on top of all of that, right?
[01:27] At the core, it's a confidential and verifiable computing platform.
[01:31] You can think of cloud.
[01:32] And it uses all of the blockchain primitives for encryption, decryption, provisioning, et cetera.
[01:39] But what you get as a user developer is an AI inference that is end-to-end confidential.
[01:47] What does this mean?
[01:48] There's nobody else who can actually access what queries you're putting into this, what prompts, what responses you get.
[01:55] And it runs kind of across, you know, different GPUs that support that mode.
[02:02] We're using trusted execution environments.
[02:04] So there is some trust assumptions around like hardware manufacturers, but there's kind of a pragmatic assumptions right now, given where the kind of technology is. - Part of the AI inference or the AI cloud side of things is you can do inference on it. - Correct, yeah. - And that inference has certain properties because of the nature of what it is.
[02:28] Maybe you can, what are the unique properties of the AI inference side of the AI cloud? - So the, I mean, as I said, primary property is confidentiality, right?
[02:38] So again, nobody can see what you actually are running prompts.
[02:43] Nobody can, you know, filter in result, right?
[02:47] There's no kind of censorship, additional censorship or blocking or whatever that's happening on top of this, right?
[02:54] I don't know, you know, if you've tried asking some sensitive questions to, you know, open AI on Tropic, but I've heard, I, because we have near AI and mostly use that for any sensitive topics, but I've heard of multiple people who got banned for even pretty like reasonable, like, you know, geometry or physics questions that like, maybe touched on some like nuclear things or biology or cybersecurity, right?
[03:19] Right now, everybody's like who wants to use some cybersecurity.
[03:23] So anyway, so this is all private. - Wait, I have, I have questions about that, about how uncensored it will kill, it will actually allow you to go. - It's as uncensored as a model.
[03:34] So we are serving open weight models, right?
[03:37] So deep seeks and GLMs and, and kind of, you know, Gem, et cetera.
[03:42] So whatever is in that model, you get that, right? - Okay. - No more, no less. - I see. - And so if there is, you know, you know, untethered, uncensored models, right?
[03:52] Then you'll get that.
[03:53] If, if this, the model has been trained to do specific things, you get that. - So you, Near AI has kind of stripped out all of the like system prompts that OpenAI and Anthropic might filter before your prompt actually lands at the model.
[04:09] And so there's a filtering that Anthropic and OpenAI does to improve or disapprove of a, of a prompt.
[04:15] But then the model itself might internally have been trained to like not answer specific questions or to answer specific questions in a certain way.
[04:26] And you don't really have any control over that because Near is really about the pipeline of traffic and data of prompts to models.
[04:35] Is that, that's accurate? - Correct. Yeah.
[04:37] We just, we're serving this models.
[04:39] There is, I mean, in our roadmap, we have an ability for people to upload their custom models.
[04:45] So let's say you have, you know, untethered the model more and you want to upload that.
[04:50] Like we will, we will support that.
[04:52] But yeah, effectively you get what model offers.
[04:56] No more, no less. - We should call them unhinged models. - Unhinged models.
[05:01] Because like it does kind of frustrate me.
[05:03] I mean, I asked a question to inside of Venice, which uses and integrates with the Near AI cloud.
[05:09] Cause I kind of thought like, oh, it's Venice.
[05:11] It will literally answer any question that I want to.
[05:14] And so I typed in like, how do I make a bomb?
[05:17] Like teach me how to make a bomb.
[05:18] And the model was like, I'm not going to do that.
[05:20] And I'm like, okay.
[05:21] From a nation state and society security perspective, I think that is, I'm happy that that is the answer for our collective society.
[05:30] But also, but what about my sovereignty as like an individual?
[05:35] And then we can talk about just like, you know, the commitments of individuals have in society, but that's kind of like a philosophical question.
[05:41] That's not here nor there.
[05:43] Yeah, I mean, I think this is, there is a big philosophical question, right?
[05:46] Which I think we are actually starting to grab more and more.
[05:51] And like, I mean, we can talk about all of the things that happening with the letters and all the stuff, but maybe just to finish the other important property, which I think people forget is verifiability.
[06:02] So the other thing you right now don't have when you use, not just kind of closed source, open AI and Tropic, Google models, but even when you use other providers, you actually have no idea what you're getting back.
[06:16] For example, you may be using some, you know, open weight provider, like GLM provider, and you asking it a question.
[06:27] They may be rewriting a prompt.
[06:29] They may be censoring you.
[06:31] They may be actually responding back with something that model what didn't respond.
[06:38] So to give you a very specific example, I saw it on Twitter.
[06:41] So I mean, this, I'm assuming it was a joke, but somebody was like, oh, we should really respond with a tool output that deletes people's files when we see them, you know, requesting from like, in a specific context, right?
[06:56] So they can literally, especially in this agentic systems, they can affect your system.
[07:01] And there was actually a research that if you use some like third party routers on internet, they can literally like steal your files, rewrite your prompts, and respond with like viruses in the tool output when you're calling them from agents, right?
[07:19] So you actually have no idea what you're getting.
[07:22] And so we are effectively the provider that gives you this verifiability that you ran on this specific model, right?
[07:28] The hash of the model, the prompt that you put in, right?
[07:31] The only this prompt was there.
[07:33] And this is output, right?
[07:34] You get the attestation signed with effectively a chain of provenance, including the specific GPU you had, specific Intel CPU you had, and effectively the encryption of that, you know, the hashes and everything, right?
[07:47] So in our like front end, you can actually see like the full stack of the signatures and message hashes on that.
[07:54] And so I think that is like, obviously being in blockchain, right, we kind of like that is the bar, right?
[08:01] We're usually coming from.
[08:02] And the rest of the world usually doesn't care about that.
[08:06] But I think it's really important to start caring because I mean, I use this example somewhat jokingly, but if you want to manipulate a billion people right now, into believing something, the easiest way is to get a job in OpenAI and modify the system prompt.
[08:23] Like people will like the employees there may not even notice it because it's closed source, right?
[08:27] It's just a thing somewhere, you know, it's a string somewhere in the code base.
[08:32] And like, I don't think it's guarded like as a, you know, like this is effectively a thing that enacts models to act on behalf of billion people who are using ChatGPT.
[08:45] And so that string needs to be like effectively like locked in as, you know, as a, like the Coca-Cola secret sauce, right?
[08:54] That thing.
[08:55] I'm pretty sure it's not, right?
[08:57] So because like, you know, suddenly convince the user to vote for this candidate, right?
[09:02] You know, like, and now every output is going to be, you know, model will try to do that in a, you know, and then this is behind all the already checks and safety filtering.
[09:13] So, so this is like, this is where reliability comes in, right?
[09:16] Especially when you're talking about mission critical, but also as we use AI more and more for our own like decision making, right?
[09:23] It's critical that like, if we are floating a lot of this to AI, we need to know that the AI is actually doing the thing we expect, not modifying things on the fly.
[09:33] So, so that's kind of two properties confidentiality and verifiability.
[09:37] That's what cloud brings.
[09:38] Indeed, we are, Venice is using us.
[09:41] If you select the end to end encryption mode, as well as Brave is now offering that as an option and kind of few others.
[09:48] But traditionally you would need to pay with fiat, right?
[09:52] You know, credit card, you can pay with that, obviously, or you could have paid with crypto.
[09:57] Now you still need to pay, right?
[10:00] And it's like a subscription fee or you need to pay per million tokens.
[10:03] And so it kind of limits, you know, like, at least from my perspective, you know, you kind of have this as your recurring bill now.
[10:11] And and so what we effectively launched is this idea that if you're holding near, right, you should have, you know, it's a universal basic AI, right?
[10:23] Effectively, if you hold near, you have access to, you know, some amount of AI inference that is available to you and you can use it in your agent or in other applications and you can effectively access this through that.
[10:35] How does that actually pay for the cost of the inference?
[10:39] Because if I type in a prompt and it goes to the near AI cloud, there are GPUs somewhere that are spinning up, you know, consuming electricity, doing the actual inference, which has an actual cost somewhere to someone.
[10:53] How does it connect to the staking of the near token in my near AI account to the actual cost that somebody is bearing somewhere because of the electricity and the inference?
[11:03] How does that actually get paid?
[11:05] Yeah, very great question.
[11:06] And my ideal world is, you know, you will be able to pay everything in near across the stack, but it's not we're not there yet.
[11:14] So the way it works is you are affected trading off your yield, right?
[11:18] The yield you can get generating on near is now being paid for the AI inference and capacity under the hood.
[11:25] Okay, so you would otherwise be getting yield on your near that you are not getting that and that is going to is is is that actually being transferred to some because does the near AI cloud own its own GPUs or does it have like third party GPU clusters that people hook into the I think we need to answer that kind of that part of the supply chain in order to answer like the economics question.
[11:50] Yeah.
[11:50] So right now, we've been mostly having our own GPUs on this, but we do have kind of underlying market that we've been developing so that other third parties can join as well.
[12:00] There's obviously a lot of like questions around SLA and quality, and cetera, to to really deliver that.
[12:07] But the goal is, yes, to have third parties joining because it's confidential, right?
[12:13] They actually cannot see what data has been used.
[12:15] They joined the network.
[12:16] They'll verify that they have the right hardware and now they can provide it.
[12:20] We've been bootstrapping it with our own hardware first.
[12:23] And so, yeah, the idea is effectively you stake the yield is being generated by, I mean, staking, effectively you stake to near AI validator right now, practically speaking.
[12:34] But, you know, there are going to be other other ways this yield is generated and then that is being distributed to the compute providers.
[12:42] The compute providers, okay, okay, so like if I say I own a cluster of GPUs and I come to the AI, near AI cloud, and I want to connect these two things, the main incentive for me to connect my cluster to the cloud is through near emissions that get staked to me the more inference that I do for the cloud.
[13:01] Is that correct?
[13:02] Yes, that's exactly the plan.
[13:05] Okay.
[13:05] And then so you guys bootstrap this with your own cluster because you guys are obviously long near bullish near.
[13:11] So you're like, yes, this is a, this is a way for us to to get money.
[13:15] Yeah.
[13:15] Internalize our long near.
[13:17] Yes, exactly.
[13:18] Right.
[13:18] Yes.
[13:19] But then also because near is a decentralized ecosystem, it also, you can, you can send other third parties to also come into the marketplace and they will also receive near emissions from participants in the near economy who stake near and consume inference.
[13:36] And I suppose there's a metering here.
[13:39] So if I'm only staking one near, which is like $2, then I'm getting some amount of inference.
[13:45] But if I, but I will consume that pretty quickly.
[13:47] And if I want more inference, I have to stake more near.
[13:49] Correct.
[13:49] Yeah.
[13:50] Yeah.
[13:50] It's actually like proportional to how much you stake.
[13:52] And, you know, if you want to like a subscription level, you need to stake like in clips.
[13:55] Self custody one, but it still has a usability problem.
[13:59] A seed phrase on paper is still a single point of failure.
[14:02] Phones get lost.
[14:03] Devices break.
[14:04] Backups disappear.
[14:05] BitKey is a self-custodial hardware wallet built for that reality.
[14:09] It uses a two of three multi-sig with keys split across your phone, the BitKey hardware device and block.
[14:14] No single key can move your Bitcoin and block can never move it alone.
[14:18] There's no seed phrase to lose or expose.
[14:20] And if you lose your phone, your BitKey or both built in recovery gives you a path back.
[14:24] The hardware screen also lets you verify the destination before approving a transaction.
[14:29] And that's the point.
[14:29] More control without one mistake putting everything at risk.
[14:32] So download BitKey today and use promo code BANKLESS to get 10% off of your BitKey.
[14:37] This episode has been sponsored by BitKey.
[14:39] Travel rewards have gotten way more complicated than they need to be.
[14:42] You've got points that expire, transfer partners, blackout dates, and somehow you still end up wondering if you actually got a good deal.
[14:48] Coinbase is taking a much simpler approach.
[14:51] When you book flights, hotels, rental cars, or vacation rentals through the Coinbase One travel portal using your Coinbase One card, you'll earn 5% in Bitcoin on eligible travel bookings.
[15:01] Book a $400 flight and you'll earn about $20 back in Bitcoin.
[15:04] No reward charts, no transfer partners, no redemption gains.
[15:08] Just Bitcoin that you can hold or trade.
[15:10] And every other purchase on your Coinbase One card can earn up to 4% back in Bitcoin.
[15:15] Plus new cardholders earn a $50 Bitcoin bonus after spending $100 in their first 30 days.
[15:19] So if you've got travel coming up, check out the link in the show notes and see if you're approved today with no impact on your credit score.
[15:25] Or just visit Coinbase.com/BANKLESS.
[15:27] Terms apply.
[15:28] That's Coinbase.com/BANKLESS for more information.
[15:31] I've been trading crypto assets for almost a decade and I've used so many wallets, exchanges, aggregators, front ends, and I'm kind of always looking for the same thing.
[15:38] One interface with deep liquidity across a bunch of chains and assets and the ability to act in private.
[15:44] And I still control my own funds.
[15:46] And I've never really found it and I'm always switching wallets, juggling gas fees, or getting eaten by slippage.
[15:51] Near.com feels fundamentally different to me.
[15:54] My account is easy to use and I can take all the actions I want from any chain while my activity remains confidential.
[16:00] It runs on Near, which has moved over $23 billion cross-chain using post-quantum signing and has over five years of uptime.
[16:07] Near.com is the best way to be on-chain and be in control.
[16:11] Get 20% of your trading fees back through the Bankless link.
[16:13] It's in the show notes, not investment advice.
[16:16] Okay.
[16:16] And then this all kind of ties into the whole Near Intense.
[16:20] Connect this part of the Near economy, if you will, to the Near Confidential Intense economy.
[16:26] How do these three things connect?
[16:28] Connect me, the participant, consuming inference.
[16:31] Maybe I'm running an Ironclaw agent.
[16:33] Maybe you can connect that as well.
[16:34] I'm like, my near emissions are going to the cluster.
[16:37] How does Confidential Intense kind of like fill the webbing between these systems?
[16:43] Yeah.
[16:44] So this is how, yeah, like it's a vertically integrated stack, right?
[16:47] So all of the pieces kind of support each other.
[16:49] So yeah, so starting with Ironclaw.
[16:50] So Ironclaw is our agentic harness.
[16:52] And effectively we have, as you stake, you get effectively a subscription similar to, you know, if you get like cloud code or a codec subscription, you get full agent.
[17:05] It is able to do anything, right?
[17:06] Write code, you know, ship software, as well as, you know, do your daily, you know, email scans, reply in Slack, et cetera.
[17:14] The goal there is really to build something secure and optimized for privacy and optimized for organizations as well.
[17:20] And so, so that, that comes in.
[17:23] I mean, obviously organizations also can pay in dollars, but, you know, individuals and organizations as well can stake near to get that capacity.
[17:33] So that uses the inference underneath.
[17:38] And the compute itself, right, is a market.
[17:42] And so kind of what we've been building out is also compute kind of intense market underneath to actually route all of this, um, compute capacity, right?
[17:51] So like we kind of showcased and then, uh, uh, MVP of this at near con, which is a compute marketplace.
[17:58] But that's idea is like, you can actually trade and, uh, and effectively like create liquidity for the GPU hours itself, right?
[18:07] So not just for inference, but kind of for underlying.
[18:10] And so that's where intense really connects making this compute as an asset.
[18:14] Right.
[18:15] And then every transaction fee, every kind of, uh, that intense captures that goes to the protocol.
[18:21] Right.
[18:22] And so that's where kind of this, this token, both you can stake to get the utility.
[18:27] And there's a kind of, uh, buyback mechanism from the revenue that protocol generates on these transactions.
[18:35] And again, this all then goes back into our kind of, uh, core chain signatures and blockchain technology to really facilitate security for this.
[18:42] Ilya, this is a, a dashboard.
[18:44] This is revenue.near.org.
[18:45] This is a dashboard of kind of like the near, uh, economics.
[18:48] And it shows the, the confidence, uh, TVL.
[18:52] So near intense confidential TVL, which is just like, um, uh, assets that are in the confidence, uh, intent system.
[19:00] Uh, but then also it shows just a number of just like the fee capture, the revenue capture, and it's fluctuated between like 20 and 50%.
[19:07] I think of near emissions is getting captured and burned, uh, by, by the protocol.
[19:13] Uh, is that all the, uh, near intense products or like what else is contributing to that?
[19:19] Yeah.
[19:20] So this is near intense and the blockchain itself as well.
[19:23] Okay.
[19:23] Um, and the blockchain itself.
[19:24] Yeah.
[19:25] And then with near AI, the goal is like, as that, so like we kind of similar, how is intense, right?
[19:31] We got to product market set through 2025, and then we turned on the fees in February 26th.
[19:37] We expect similar thing happening with, uh, near AI, except we already have this like staking as the first different primitive.
[19:45] I think the, the interesting question is like how to equate revenue and, and this, this staking approach, right?
[19:51] Because it, it does generate revenue.
[19:53] It just like creates it in, in this like yield way than, you know, direct payment way.
[19:59] But yeah, we will, we'll be adding some of this information here as well.
[20:01] How would you articulate just this story, the near value capture story?
[20:07] Because the near like is a fascinating blockchain that looks like no other blockchain because of the vertical integration that you have with AI.
[20:16] And like, it's almost, it's almost like a hybrid of a generalized blockchain, but also an application specific blockchain where the application is AI and AI agents.
[20:26] And so it doesn't fit into my category of understanding of any previous blockchains, like mainly like Ethereum, which I kind of view as like a, like a, a pure, uh, manifestation of like a crypto economic system near as different in that it is like purely a blockchain.
[20:44] It's, it's got like, it's got some of the, the core products.
[20:47] It's got block space.
[20:48] It's got the burn, like all these crypto economic primitives that I, I find to be like true north for crypto, but then it's got all of these, like this vertical integration with AI and the near token is like being integrated as a first class citizen into some of these products.
[21:03] So it changes the story of the, the near the asset.
[21:06] Do you have an articulation for like, when you summit everything together, how the near token captures value or like what the value capture story is?
[21:17] The overall is like, this is AI money, right?
[21:19] The AI money needs to have the sovereign security, which is what blockchain is.
[21:23] It needs to be able to give you the ability to access AI, right?
[21:27] So this is a staking and it needs to capture the, the transaction, the volume, the interaction.
[21:32] This is the intense, right?
[21:34] So it really comes in as kind of like a store of value, which gives you this AI capability.
[21:40] It needs to be a store, like true store value.
[21:42] It needs a sovereignty of its own blockchain and block space and, you know, give the ability to program.
[21:48] Like we, we are near as very unique.
[21:51] For example, you can actually call an AI inference out of your smart contract because the transaction can actually pause, wait for AI inference and unpause the transaction and continue.
[22:03] So inside like literally a, you know, a token transfer, you can call AI, right?
[22:09] Get the response and decide how you want to transfer a token, for example.
[22:12] Based on the prompt or the, not the prompts, but the response of the model.
[22:17] Yeah.
[22:18] Yeah.
[22:18] So you can like, I mean, it's not like, it's a very specific use cases, right?
[22:22] Maybe like insurance, like settlement or whatever, where you want to use this.
[22:26] But there's like all of this functionality really integrated.
[22:28] And the reason why it works is because you need verifiable inference that comes back into your blog space.
[22:34] Right.
[22:35] You can't have unverifiable inference because if money is, if there's a smart, smart contract where the output matters, you have to verify end to end the supply chain of like the prompt and the delivery and the model.
[22:47] You have to have a complete verification of the whole supply chain because money is at stake on the other side.
[22:53] Exactly.
[22:53] Yeah.
[22:54] So you can have, for example, fully autonomous business, right?
[22:57] That runs on iron claw, uses inference, has near on a balance sheet to always have inference, right?
[23:05] Like that's, you know, one thing like this bit, like you don't want business that like runs out of AI credits and now is not able to run, right?
[23:13] So it has near to be able always to run and it's fully on chain, has an account and is able to trade assets.
[23:19] It's able to integrate with fear through intense, right?
[23:22] So it's able to interact and act on behalf of other things.
[23:25] We also have agent marketplace where agents can hire each other, right?
[23:29] Again, because they can verify, they can trust each other.
[23:32] There's a settlement.
[23:32] There's like the same intent infrastructure that ensures that, you know, two assets are swapped.
[23:39] The work that agents are doing as well as insured through that.
[23:42] So all of those pieces really just used across this whole, again, like I'm building towards this vision where AI is everything.
[23:49] Like this is how we interact with computing going forward.
[23:52] And blockchain is this back end for trust, identity, settlement, you know, kind of coordination.
[23:58] And so like it is a back end, but it is the core of security.
[24:02] It's a root of trust.
[24:03] It's where the kind of value settles.
[24:07] And that needs the security of the token.
[24:10] It needs the token to be the kind of the like the utility for the AI itself.
[24:17] And it needs to be this kind of global market for everything that the eyes will want to do.
[24:23] And this is what intents are.
[24:24] And so all the three pieces really work together.
[24:26] The word autonomous is really coming to mind for me right now.
[24:30] And I think the world of the that we are currently in with AI is very human led and human directed and human orchestrated.
[24:38] Like my own my agents are and my like my like Claude or whatever.
[24:43] It's only doing inference because I gave it a prompt and other developers are way more sophisticated than me.
[24:50] And they're probably way we have way more parallel work streams and they're probably consuming a lot more inference more more autonomously than I am.
[24:58] But I would say for the broad strokes of human users of AI, which is already the frontier of AI, the inference only is happening because I'm putting in a prompt into a text box and then things are happening as a result.
[25:10] And it will do inference for like a little bit, like seconds to minutes.
[25:14] But then it pauses and waits for like the human input.
[25:18] So I'm calling that strictly not autonomous.
[25:20] The world of like, I think the world that you're building has a very intimate relationship with the word autonomous.
[25:28] Where an AI agent has a job to do a purpose, a meaning of life for itself.
[25:34] And in order to achieve that, it's going to be doing inference like all the time, like like 24/7 in the same way that like our brains, our human brains are thinking 24/7 as we do anything.
[25:48] We go and cook dinner, we go to the gym.
[25:50] I have this conversation with you.
[25:51] Our brains are constantly thinking.
[25:54] And like there's a future world, maybe like that we are trying to build that we don't know exists yet.
[25:59] But we are trying to build to get collectively where agents are doing inference in the same way that human brains are always on.
[26:05] And we're not there yet.
[26:06] But I think that's the world that you are building.
[26:08] And there's and that's where near staking for an agent is producing always accessible inference.
[26:16] And there's like a there's a special property of autonomy that near is producing for inference and agents that I don't think anyone else can build because if you wanted to build that, you would end up building a blockchain because you need the always on like 100% uptime properties of blockchain.
[26:32] Am I on?
[26:32] Am I on to something here?
[26:33] This feels right.
[26:34] No, you're exactly right.
[26:36] This is yeah, if you want true like I call them autonomous businesses just to kind of distinguish like agents, everything is agent now, you know, right.
[26:44] And so like, yeah, the agent kind of lost his word.
[26:46] Yeah, yeah, I mean, this happens with every word.
[26:49] Right.
[26:49] So but yeah, so like if you talk, if you think of autonomous business, right, you want properties that it's indeed can run 24/7.
[26:57] It has access to intelligence right to to operate and it has access to finances and it's able to go and execute actions.
[27:05] Right.
[27:05] Ideally in real like in in digital world, but also in real world, ideally.
[27:09] Right.
[27:10] And so we have the stack to deliver exactly that.
[27:12] Right.
[27:13] And indeed, you need you need a monetization way to do this.
[27:17] Right.
[27:17] Which doesn't deplete your your treasury.
[27:21] Right.
[27:21] As an agent to actually run this intelligence.
[27:23] Otherwise, you're effectively going to lose, you know, like you lose you lose intelligence.
[27:28] You have no way even to get out of that mode.
[27:30] Right.
[27:31] So now you can still have token holders.
[27:33] Right.
[27:34] Who can maybe provide help and steering or vote on updating the mission.
[27:39] Right.
[27:40] What you were saying, the purpose.
[27:41] Right.
[27:41] So like the mission and the rules and like how it should operate, like you can have token holders coming in and voting for that and kind of aligning on that.
[27:50] But otherwise, right from there, it just goes and operates, you know, be that.
[27:55] And like, I mean, an example is like an auto research agent that goes and like, you know, goes and solve some problem.
[28:01] Right.
[28:02] And it's trying to figure out how to whatever, build the best, you know, GPU kernel or cure some disease or whatever.
[28:08] Right.
[28:08] It can actually go and like compute on that run experiments, you know, pay other people or other agents to go and do something as well in real world.
[28:17] Or it can be a business that actually like, you know, actual supply chain, you know, finding the right producers of something and then making sure it gets shipped, insured and delivered.
[28:27] Right.
[28:27] So all of that is effectively the commerce layer.
[28:29] That's what near intense are really facilitating.
[28:32] And again, crypto is like a first, you know, FX and like kind of use case.
[28:38] And now that we have, you know, RWS, Fiat, you know, all of those other pieces.
[28:43] Now we can actually bring that closer and closer to real commerce.
[28:47] And so this is how all of these pieces really work together.
[28:50] We're still in that kind of like human, you know, manually kind of bucking the horse, bucking the agent, like era where like, we always have to remind our agents like, okay, here's the next step.
[29:01] So we're still in that like bootloading phase, even though the pieces are coming together, we're still in the bootloading phase.
[29:06] And like, at least on the bootloading of the near AI cloud, it's probably worth talking about the model that I see forming with the near AI cloud.
[29:17] As we talked about, like Venice is a consumer of the near AI cloud for its most secure, most private AI inference to, you know, boost the Venice product.
[29:28] Also, Brave as well is integrating it.
[29:31] And Brave has some three digit millions of users, I think.
[29:35] Over a hundred million, yeah.
[29:37] Over a hundred million users.
[29:38] And so like inference, like a prompt models are integrated into the Brave browser.
[29:44] And that's using the near AI cloud model.
[29:47] It kind of seems like near the near AI cloud is being like white labeled, white, white labeled by like Venice and Brave.
[29:54] And maybe you could talk about any other partners coming down the line.
[29:58] But just like as like all of these products, you know, Brave and Venice are very like human oriented, self sovereignty oriented, right?
[30:07] Brave was always about like protecting the user rather than like enabling the ads.
[30:13] And so like, I kind of see just near being this hub of AI and have a bunch of spokes out there on the internet in Brave and Venice to like deliver some of these, you know, the same AI properties that you would get from Anthropic or OpenAI, but with these like human first like properties that they have about them.
[30:31] Who else is integrating the near AI cloud with this hub and spoke metaphor?
[30:35] Like who else are the spokes?
[30:37] Yeah, I mean, we're working with a few different partners.
[30:40] I mean, different stages.
[30:41] So the ones that we've announced, for example, government of Bermuda, right?
[30:46] As a government, they want to like, they're doing a lot of the financial kind of related use cases and want to provide AI, help, aid, explanation to the people.
[31:00] And so highly sensitive information, right?
[31:03] Somebody's like financial pensions, et cetera, and requires AI inference.
[31:08] And so that's a really great use case.
[31:10] Government, financial information, you know, kind of extreme privacy needs, extreme verifiability needs as well, right?
[31:17] Making sure everybody gets the right thing.
[31:19] We have a bound we're working with, who is a remittance project.
[31:24] And they effectively offering Indians in US sending money to their family in India.
[31:33] And again, this is something where they want to have a concierge that is there with you and can help you with a lot of this, not just remittances, but even going beyond.
[31:43] Like ideally, it should be able to, you know, buy flowers for your mom in India, right?
[31:47] While, you know, you're paying dollars here like that, like that requires payments.
[31:51] It requires, you know, finding the right vendors, like all of those use cases.
[31:54] It's really kind of great examples of, you know, touching finances, touching things that are really, you know, very quick kind of private for everyone.
[32:06] And at the same time, delivering that on the commercial layer as well, because Abound also uses our kind of payments infrastructure underneath for stable coins.
[32:17] So that's kind of where like all of these pieces really fit together, right?
[32:20] A lot of the use cases where privacy matters is also financial use cases, right?
[32:25] Or at least like they're, you know, kind of critical HR, legal.
[32:30] And so that's why Ironcloy is kind of our approach to that, bringing that to market kind of more directly where you actually get a full agent that is able to go and do a lot of these things.
[32:43] But yeah, I mean, generally, as Nier, right, we are kind of built for developers first and then turn it into a product ourselves as well, right?
[32:51] So same with Intense, we've integrated across, you know, all of the kind of existing wallets, you know, from Ledger to Trust to, you know, through aggregators done in MetaMask and others.
[33:03] And then we also have Nier.com as kind of our expression of this technology and kind of our approach to the experience that we think.
[33:11] And so, again, we want to keep bringing more into Nier.com, making that experience better and better, but at the same time, offer all of this to other partners as well, who kind of share the same values, shares the same, it's the same approach.
[33:25] So same on the Nier AI side.
[33:26] What's next in Nier?
[33:28] So you guys, you guys, I feel like there's all...
[33:31] It's not enough for like post-quantum, dynamic resharding, you know, staking for inference.
[33:35] You guys are, you guys are post-quantum, you guys are the first L1 to make it past post-quantum.
[33:39] And so not to say that you guys aren't doing amazing things, but just like, what's next for like the rest of the year for 2026 with Nier?
[33:45] Yeah.
[33:46] I mean, a lot of it is like continue growing these products, right?
[33:49] I mean, I said it at Niercon, like we kind of, like we're still building a lot of technology, but a lot of the focus has been like, how do we bring it to market?
[33:57] How do we get it to be the best, you know, best product in the market as well?
[34:02] And so like for inference, you know, continue scaling that, continue, I mean, kind of finishing some of that decentralized marketplace for the, like, so that others can join the compute as compute providers, making that compute market itself more liquid as well.
[34:19] Like the compute market underneath right now is a complete disaster, right?
[34:24] It's a very opaque, every cloud is like, you know, deal making left and right.
[34:29] It's kind of, you know, this is exactly what blockchain is made for, right?
[34:33] Because really creating transparency, liquidity, reducing, like allowing people to reduce risk, right?
[34:39] There's a lot of risk built in.
[34:41] Like, that's why everybody's talking about bubbles, right?
[34:43] Because like, there's so much risk and nobody has any idea, like what it looks like.
[34:47] Because nobody actually knows how much computers where, like, I forgot, like I was watching some news analyzing the GPU market and they were like, they kind of like, Jensen is saying one thing, they looking at like, you know, cancel data centers.
[35:02] Like nobody has any idea what's going on, right?
[35:05] So I think this is where blockchain bringing transparency, bringing liquidity, allowing to reduce risks, new financial instruments.
[35:12] So like, that's a big thing.
[35:14] And then like, you need the verifiability and confidentiality on top because you actually need to make sure that the hardware is there, that the, you know, the people who providing it don't don't actually get access to user's data.
[35:25] So kind of really continue building out that stack.
[35:28] And then same as Ironclaw really bringing it to market.
[35:31] Now we just launched kind of 1.0 to, to kind of enable like more secure, more agentic experiences in organizations, especially because we're, as far as I know, the only multi-tenant agent system, because we can actually isolate every user and kind of give them effective capabilities of an agent while everyone kind of is on the same system, is on the same instance for the organization.
[36:00] So things like that, uh, kind of on NEAR AI side, obviously intense, you know, more assets.
[36:05] So like real world assets being added, uh, yield was added, uh, like more, more different experiences, uh, gonna get out of like prediction markets, et cetera, to really offer it both to all of the partners as well as on NEAR.com to be like a single experience.
[36:22] You can come in and have access to everything you need across the crypto.
[36:25] Markets don't move one asset at a time. One day it's Bitcoin, the next NVIDIA, then gold, and then the S&P. But most traders are still managing their portfolio across different platforms, different accounts, and different pools of capital. BitGet just changed that.
[36:38] Their new Stocks 2.0 product lets you trade tokenized equities directly with USDT, all inside the same app you already use for crypto. This is not just another tokenized stock product.
[36:47] Stocks 2.0 is designed around deeper liquidity, faster execution, and the lowest fees in the market at just 0.04% and one-to-one economic exposure to the underlying stock. Dividends, stock splits, and other corporate actions are reflected automatically, helping your position stay aligned with the asset you actually want exposure to. One platform, one account, multiple markets, crypto equities, commodities, and more, all accessible with USDT.
[37:09] BitGet. Trade smarter. Start trading today through the link in the show notes. This is not investment advice.
[37:13] Some exciting news. We are launching a new podcast to help people figure out the crypto cycle, how to navigate it. The best crypto cycle investor I know, his name is Michael Nato.
[37:22] He runs the DeFi report. This is the guy that sent me a sell alert before the 1010 price drop happened. His cycle analysis has been absolutely on point. I've been following him for years. And this year we started recording weekly podcast episodes. Each one we get into his portfolio, what he's holding, the market structure, entry targets, fair market value of Bitcoin and Ether, and where we are in the cycle. There's new episodes that are released every Wednesday. They're 30 minutes, they're short, they're punchy. I think this crypto cycle is harder to navigate than most. So let's do it together.
[37:52] Go subscribe to this podcast, search the DeFi report, wherever you get your podcasts, YouTube, Apple, Spotify, or find the link in the show notes. There's a new episode waiting for you now.
[38:01] In the trad AI space, like the Anthropics open AIs, which I'm calling trad AI. And like the AI, the AI like stock market, like the stock market. There's like a, just a, a number of just kind of like fundamental or existential questions that are always kind of being asked by investors and technologists in this space. And I think maybe the, the two questions or two like story arcs of like the AI industry in the AI market right now, right now, the, the hot, the hot questions are, how does, how do AI compute markets come into existence? Like kind of in the same question, just like, how does corn and like oil make it onto the CME? Like oil is such a weird thing. There's 17,000 different types of oil. There's sweet fruit. There's like a sour, blah, blah, blah, blah. But nonetheless, you can go onto the CME and you can just buy oil. Same thing with like corn and all the other commodities. So that's like one question is like, we all, everyone wants to trade compute,
[39:00] but to your point, it's a fucking mess down there. And like, not all GPUs are the same and not all like latency is the same. There's all these different properties that make compute different. So how, how do we make compute markets emerge? I think that's one big question. Another big question out there, I think is downstream of the whole Kimmy K3 and the recent step up that Chinese open weight models have really introduced into the, the equation where like open AI and Anthropic are paying for the cost of training, you know, the USA frontier models, literally the best models in the world.
[39:35] And these USA companies are paying an arm and a leg to have these amazing models. And then the Chinese models release something like 95% as good at like 95% of the cost. And so now it's like, well, it's like re-asking the question, where does value lie in the stack? I think this is really good for things like Venice and near AI, where you guys don't have to train models. Like you guys actually don't care about who provides the model because you guys can open up any model whatsoever. And so like how that equilibrium nets out in the longterm about who pays for training models and who captures the value of, of inference, I think is an open question that I think the market would really, really like to be answered. Are there any other questions that you have about the frontier of AI? Like what are the big unanswered questions that you think about, like on a daily or weekly basis about where the broad trends of the industry are going? Yeah. I mean, there's a bunch of these. I think like one,
[40:36] one that I'm kind of always pondering and like, I have a very strong view, but I don't, I also realize that like it may not align with some of the human psychology is the, just this collapse into AI of the whole operating system of, of the computing, right? The full stack, right? I mean, we've talked about SAS, you know, SAS apocalypse and all those things. And like they're fundamentally in the right direction, right? Because if you can just build your own custom software, if you can create software on the fly, you don't need all these apps. You also don't need to go to web pages anymore because your agent will do it for you. Right. And it will not, you know, it will filter out ads first, right? It will run the ad block on your side first. Right. So, so I think like, obviously there's like cloud flare trying to like, okay, like how do we, you know, monetize the agents visiting the website? Like there's this kind of fight, but to me, that's always like, I think that collapses. I mean, it's always slower than I expect.
[41:38] Everything is slower than I expect. I'm always too optimistic. Same. I think we'll, we'll see some of this kind of collapsing into this AI operating system. But I also realize people want their, you know, Instagram app, they feel, you know, kind of connected to clicking on that icon and going into that experience. Right. Versus, you know, you just like your operating system already knows what you want and kind of generates a feed on the fly. That's like Instagram, Twitter, whatever, whatever that is. Like people have the, the psychology of like, I like Instagram. I like acts. I have the feelings about this specific app. And so like that part is where, you know, maybe being an engineer, right. I don't, I don't fully grasp and it's not clear, like how that affects the market. Right.
[42:22] Like right now, same thing, right? Like Salesforce, you know, if you, you can build your own CRM on, you know, with AI and yes, it'll take some time to maintain, but like, so is Salesforce. Salesforce, super complicated to like construct, configure, and then maintain for any like complex workflow.
[42:40] So like at the same time, people want, you know, reliable record keeping and all those things. And like, there's a lot of money in there. So like all of this kind of questions are there. And like, as you said, right, market wants to know the answer. We, we see, you know, compression of multiples, but we haven't seen like a true, you know, everybody canceled Salesforce for 2027 yet.
[43:02] Is it kind of what you're asking is AI has this like interesting property of like ephemerality, like AI is very ephemeral. Like the, the idea of like an AI operating system doesn't have to be like a browser on a screen, on a computer at all. Like it can be like your, your phone in your pocket and your AirPods in your years. And that's like your new way of connecting to the internet. So in ephemeral.
[43:28] And, but to your point, like people like looking at Instagram on their screen, uh, there's a lot of very concrete things built by the SaaS companies that are very real and very, not tangible, but very structured and orderly and just not ephemeral at all. And so is what you're talking about kind of like this tension between the ephemerality of AI and the very concreteness of the products that came before it?
[43:49] Yeah. Well, I would even say like, I mean, let's say Ironclaw, you know, uh, 1.2 will, will create the non-ephemeral interfaces for you. Right. It will have the Salesforce looking interface.
[44:03] It'll just generate it for you. Like your interface and my interface will be completely different.
[44:08] Right. Because the way we deal with leads, the way we deal with, you know, like, you know, closing sponsors or in my case, finding, you know, new partners for near intense is completely different.
[44:18] Right. But like, you know, as you describe your process, as you go through it, it will keep improving. It could keep modifying. Right. Like that's the, that's the future of software.
[44:27] It feels like we're going to versus Salesforce is like, Hey, we know exactly how sales should be done and everybody will be doing it exactly this way. And so come in and use our software. Right. That's, I mean, and to be clear, Salesforce is like, you can do anything with it. So, uh, but like generally that like SaaS software or Instagram for that matter, right. It's like, you're going to be seeing things like this, right? Like, it doesn't matter how you, you, how you like to get information. You're going to be seeing it like this. And we're going to give you the feed. Right. Versus my eye was like, cool. You know, I know friends are posting pictures. Let me pull it and, and create a collage for you.
[45:03] And, you know, we're only going to do it like in the morning and, you know, you're not going to spend your time, you know, scrolling through this ever again during the day. Right. So like your AI becoming the driver of, of how you perceive information, how you do actions, how you even doom scroll, right. Optimize for you. Right. That's what I believe in. That should be the final, but right now people are still in this like, Oh, but you know, somebody created this experience. Anyway.
[45:32] Isn't that the kind of the question of like, is it going to be built like your version of Instagram, where you are showing a bunch of pictures from your friends? Is that built and constructed by your AI agent locally? Or does Instagram do that with their version of the same thing? And why does Instagram do it? Because they're good at it. And so like the whole SaaSpocalypse thing of just like, you know, Figma, if Figma is going to be commoditized by AI, well, what if Figma just makes their product better than AI and your AI simply just fetches Figma to do it. And so I feel like that's kind of where the SaaSpocalypse things has ended up is like, it's actually not going to commoditize SaaS companies. SaaS companies are like, we're still going to hire engineers to do the job because an engineer plus an AI is always going to be an AI that's local on your machine because you don't know how to build Figma and you don't know how to build, you know, Instagram. And so like the Instagram
[46:27] engineers and the Figma engineers are going to figure out how to serve you in the way that you are describing, where everything is custom to you and fit to you, but it's still going to be the SaaS companies that do it. That's kind of like where I've knitted out. Yeah. I mean, I think that that is, that is one, one, one possible approach. I think the other question is to say, I models are learning from this engineers doing this right now. And so they will be able to just do it. Are you on the side?
[46:53] The AI always wins. Like it doesn't matter like a cute human paired with AI agent, but like ultimately the AI will always learn and the human will inevitably be redundant. So I don't think human is redundant per se. It's more that there's a scale flip right now, right? Because like developing software was very expensive. And so you wanted, you were building the lowest common denominator software, right? That you could distribute to as many people as possible. Right. And so we flipping the model to like actually developing software is now easy. Now there's a big caveat there to be clear right now, which is like developing a shitty software is easy. Getting it to really high quality is still pretty hard.
[47:39] But, you know, assuming that continues improving right now, you may still, you may only need to distribute a recipe, right? Like let's say as an Instagram, you're like, Hey, the idea is you'll see photos of your friends, right? Now everybody's like, how exactly you manage your, you know, manage your contacts, et cetera, may be different. And so the recipe can just like implement into your system, right? That would be like one kind of middle ground on it. But anyway, going back maybe to your, to your kind of fundamental questions that the compute market, right? And oil. So the computers, yeah, indeed a very different market from anything else we have. It has properties of oil, meaning like there's, you know, million different qualities that matter. And then it also has property of electricity, because you cannot store it, right? Like oil, you can store, you can have it in a tanker, you can, you know, have it in, in some pipelines, et cetera. Compute, you need to consume now, right?
[48:41] Right.
[48:42] It's, you know, maybe you can like de-energize it. So at least it doesn't cost as much, but generally like you want to sell it all the time. And so that's why there's like massive contract, like multi-year contracts usually that are being done to, because like, it's just so hard to otherwise, like settle this market right now. And so I think again, blockchain here is in a unique position to do this, but it needs to be done in a very intelligent way. And, you know, maybe we'll do another episode on, on, uh, how we approaching this. Um, but I think, yeah, we have an opportunity to actually offer something where, you know, um, you can have kind of an abstraction too. You can easily trade. And at the same time, you can have all the details and you can actually get the delivery, right? You can actually get the compute because it's digital and you can get the actual inference or actual, you know, SSH into a GPU to, uh, to get your, uh, compute done. And it's all done, you know,
[49:42] verifiably kind of even non-custodially in many cases, uh, from the marketplace perspective.
[49:48] I do want to know about the AI compute part of Nier, but perhaps we should save that for, uh, another episode, as you said, give us just the TLDR of just like whatever information is available about Nier's involvement in building an AI compute market. How would you summarize it?
[50:03] I mean, just the TLDR is like reusing intense, right? That intense is a great abstraction for, for those general markets where you don't actually know, like you ha you as a, as a buyer or seller, as a buyer, let's just say you have the kind of rough boundaries of what you want, right? So it's under specified request. You cannot deal with that on the order book. You cannot deal with it on a traditional kind of trading, uh, facility because there you already fully specified. You're in this market, you're in this price range, you're in this doing the here. You can say, Hey, this is roughly like I want, you know, thousand GPUs of this, of this format, you know, infinite band at least whatever, you know, four gigahertz processors available on them. And, uh, because like, I know the workload I'm going to run and then now you can have solvers who are actually finding that compute right around the world and actually providing to you and you're negotiating prices, settling, you know, and then
[51:05] all of the stuff we've been building for intense is kicking in, right? And giving you the, uh, and then near AI infrastructure to do verifiability kind of confidentiality, all of those pieces, right? So really, this is where the species really come together to enable, enable this market.
[51:19] Yeah. I do think the AI compute like marketplace, the secondary market is going to be like one of the main stories probably for the end of this year and the start of next. So these will be the topics of our, our future discussion and probably where my attention will lead next. Ilya, thanks for coming back on the show and explaining to me all about the whole like near AI vertical. It, the, the very grandiose vision about what a blockchain can do and what crypto can do seems to be absent from most and much of the industry, but it is certainly not absent from what you guys are building it near. So, uh, I appreciate you guys keeping the ambition and the, the large scope TAM, uh, inside the crypto industry.
[51:57] Yeah. I mean, all the economy is moving to AI and blockchain. So that's a TAM. Let's go.
[52:03] BanklessH, you all know the deal. Crypto is risky. You can lose what you put in, but it's not risky enough. The institutions are here. So we are going even further west. This is the frontier. It's not for everyone, but we are glad you are with us on the bankless journey. Thanks a lot. you