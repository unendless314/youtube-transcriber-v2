---
channel: "Bankless"
video_id: "xP170cMooFo"
title: 'Tempo Mainnet: The Race to Agentic Commerce'
published_at: "2026-03-19"
duration: "1:21:51"
word_count: 72879
---

# Tempo Mainnet: The Race to Agentic Commerce

[00:00] - Bankless Station, I'm here with Giorgios Constantopoulos.
[00:04] He's an engineer at Tempo, and also joined with him is Brendan Ryan, another engineer at Tempo.
[00:10] Brendan, Giorgios, welcome to Bankless. - Good to be with you guys.
[00:13] Big day. - Thank you. - Yes. - So congrats on the Tempo launch.
[00:18] What is, I wanna know what just like the launch actually looks like, you know, day one or just in the near term, the short term.
[00:23] What are some of the first movers that are coming online?
[00:26] And then also just like kind of the first categories of activities that's happening on Tempo.
[00:31] What is just like the launch kind of look like? - We've been building Tempo since August with a lot of wonderful partners.
[00:37] We're working with Stripe on this.
[00:39] The goal is to make stable coins and web scale payments to work finally using a lot of crypto blockchain technology that we've been building over the last few years.
[00:49] Today's launch is focused on AI agents using the machine payments protocol to pay for things on the web autonomously.
[00:57] And we're continuing to push on our work on the enterprise work streams around post border payments, remittances, and things which really are truly what attracted us to the crypto world in the first place. 24/7 borderless finance and payments.
[01:10] So there's more to come on that in the next few weeks and we'll continue sharing on that.
[01:15] But today's launch was all about the agentic payments. - All about agentic payments.
[01:19] Well, I mean, there's mainnet, right?
[01:21] And, but I do notice that there is just like a very large emphasis on this MPP thing, which I think we'll go into.
[01:29] You know, I mean, Tempo is known in the crypto industry is like, you guys, you guys do stable coins.
[01:33] You guys talk about remittances, tokenized deposits.
[01:37] If, you know, somebody wants a stable coin, they might go to Stripe and Tempo and get a stable coin minted on Tempo.
[01:43] But it really seems like that wasn't really the focus of today's mainnet launch, really the focus, the emphasis is on this machine payments protocol, MPP, which I think kind of gets us into the topic of agentic commerce.
[01:55] That's what, that's what I'm reading into.
[01:56] That's what you just said.
[01:58] Why the focus on agentic commerce as like a primary, just like part of the actual mainnet launch? - The mainnet as it launched today supports all the use case that you met, all the use cases that you mentioned.
[02:12] So we already have some flows live on it, which are for a particular normal payments.
[02:19] For example, Bridge has already, Bridge, the Stripe company has already gotten some funds on Tempo.
[02:25] And we're working on further expanding support for that.
[02:28] So this continues to be a lot of the focus.
[02:30] At the same time, the AI payments world seems to be happening.
[02:35] So all of our people on the team, we use Cloud, AMP, Codex all day.
[02:41] And we're already seeing that even to us as developers, it's kind of too much to go and log into a service, auth, add card, get API key, put that API key back.
[02:52] It's just too much when we're just super charged with these new tools.
[02:56] So this really came out of our own need in a way for, okay guys, it looks like this AI agents want to do more, but they're not able to, they get bottlenecked on the human.
[03:07] Or just to give you another example, let's say I have my deep research agent and I'm browsing around.
[03:13] It can many times just improve its quality of response.
[03:16] If it had access to some piece of content that was paywalled, for example, New York Times article or anything else.
[03:22] So we just thought, hey, what if we didn't have to do anything around that?
[03:27] And what if we just gave the agent the wallet and we just let it rip?
[03:30] And we really went with that thesis that, okay, we have the enterprise stable coins things.
[03:36] These are very important.
[03:36] We should continue doing them, but we cannot ignore this wave that's coming, this tailwind about, which could affect materially the focus for everyone in the crypto payments industry.
[03:48] And as it was, we decided to really put a lot of energy, make the launch, be focused on this, and then continue with the rest of our work because it was just too important to not make a move on this. - We've already mentioned something called MPP.
[04:01] Can you describe what that is?
[04:02] And how is that different from other agentic payment standards that we've seen, something like X402?
[04:08] MPP or machine payments protocol is a open and payment method agnostic protocol for machine to machine payments.
[04:18] And I think the best way to think about it is, it is like the payment form for agents.
[04:27] So today, I think all of us are very familiar with coming on a page, you see kind of a standard payment form, it's all the same layout, but you can plug in hundreds of payment methods into that, if it's cards, Klarna, even paying with crypto, all of that plugs into that.
[04:43] And it's humans are used to that UX, it's very efficient.
[04:46] But if you expand that, and I think this is why we are so interested at Tempo about machine to machine payments is we just see it at a huge velocity and a huge compounding number, month over month growth.
[05:05] So we think as that velocity increases, you just need more efficient interfaces.
[05:09] So MPP is we view as a payment method interface, which agents can interact with really, really efficiently.
[05:19] We've done a bunch of benchmarks to make sure this is true and allows them to transmit payments over multiple payment methods, seamlessly in HTTP requests.
[05:29] So we can see this today, a lot of API services, people ordering sandwiches today, you can use it in MCP servers, but you can also use it even for if you just wanted to host a video or have some content, kind of this classical micro payments for content use case that people have been talking about since the 90s, but really hasn't been feasible just because of the interface
[05:56] it's exposed to.
[05:57] And people thought about it at the time, the status code was created in the core HTTP spec, but never really formalized.
[06:05] And we think MPP is the formalization of it.
[06:10] And we have designed it in such a way that is entirely neutral on payment method, currency agnostic works with web standards, and we actually submitted it to the IETF this morning in order to be the true spec for 402.
[06:27] And we think it's the best chance for a totally neutral approach.
[06:31] Wait, be the be the spec for 402.
[06:34] I guess maybe the question is, so we've definitely heard this story before and we're excited about it, but we've heard it more in the context of another emerging standard, which is X402, Coinbase's champion that Cloudflare has been behind it.
[06:47] I also thought somewhere in the world, like Stripe was involved as well.
[06:51] Just to be clear, is this like a competing standard to that or is it some sort of superset?
[06:57] Like how is it similar versus different?
[07:00] How much is it competitive with X402 versus collaborative?
[07:04] What does it look like in contrast to X402?
[07:08] With regards to the Cloudflare and Stripe component, Cloudflare and Stripe are both companies that are on the record that they want to be neutral and want to be supporting all of the systems.
[07:18] So today, Stripe has support for both MPP and for X402.
[07:23] Cloudflare the same.
[07:24] Cloudflare also this morning added an MPP proxy GitHub repo, where you can use to make any service MPP enabled.
[07:32] Okay.
[07:32] So from their perspective, all these platforms, they will just adopt everything and they will allow their users to choose what they want to choose based on other reasons that the protocol to differentiate on.
[07:45] Now, how do they actually differentiate on?
[07:48] I think it's three reasons.
[07:50] One is performance.
[07:52] Two is developer ergonomics.
[07:54] Three is platform support.
[07:56] And let me unpack them.
[07:58] With regards to developer ergonomics, David, Ryan, we've been in many podcasts like this together.
[08:05] Our team is a team that shipped the Foundry project, which is the thing that powers all of the hundred billion IndieFi that has existed over times.
[08:14] We know how to build, how to test developer tools for back-end developers.
[08:19] Our team also has built Wagme and VM, which are the most used front-end frameworks right now for any Web3 crypto app.
[08:27] It's used probably by 90% of every crypto website right now.
[08:31] So we really know developers.
[08:33] And I think that really manifests in our API design, in our library design, how ergonomic and how intuitive things are when they're built.
[08:42] And when we looked at the ergonomics of X42 and other things on the market, we just weren't satisfied.
[08:49] So we thought it's just easier for us to go back to first principles and think, okay, what's the simplest developer-friendly ergonomic API I could use?
[09:00] And the way that I saw it is let's go back to the basics.
[09:03] What is the most basic thing that we're doing here?
[09:06] We're doing auth.
[09:06] That's literally what we're doing.
[09:08] We're just saying, instead of authorizing with an API key, let's authorize with a payment.
[09:12] So we went back and we looked at all the literature and our basic auth, bear auth, all of that.
[09:17] And that was what informed the original design of the first iteration we did for MVP, which is actually in a funny way, what made it so easy to make it payments method agnostic.
[09:28] Versus if you look at X402 or whatever other approach, X402 is a bit tied to the facilitator, which is a very specific implementation detail almost, that should never be surfaced all the way up to the protocol.
[09:40] So we had a different approach and we said, okay, this will be too much effort to make it work with that.
[09:45] Why don't we do it with our own and see how that could work.
[09:49] Now, in the history of the web, it always has been better to have more than one solution because then these two solutions or many more solutions, then they end up iterating to what's optimal for the consumer.
[10:00] So yeah, I think there are like two different approaches that you can use to use agendic payments.
[10:05] And I think it's going to be a beautiful, you know, step-by-step on evolution of how do people make it work.
[10:11] But to be clear, it's a competing standard then to X402.
[10:14] You think it's better, but it's competing.
[10:17] I think they could compete.
[10:19] I think there's a world where they converge.
[10:21] I think either could happen.
[10:23] You could, well, technically, because MPP is more general, you can express X402 in MPP.
[10:29] And we had a draft that we hope to publish soon about this.
[10:33] I don't think you can express MPP in X402 terms.
[10:36] Okay.
[10:37] So MPP could be a superset and you say it's more broad.
[10:40] Does that, when you say it's more broad, I noticed like Visa integrating it, for example.
[10:45] So it's not just Stablecoin smart contract types of payments.
[10:49] It's also some of the traditional type payments.
[10:51] Is that what you mean by more broad?
[10:53] Like, you know, works with a Visa card?
[10:55] And Ryan, to be clear, I want to still man the X402 side, which there's a blog about X402 V2, which specifies that, okay, it will be more payments method agnostic and so on.
[11:07] That's fantastic.
[11:08] But what we have right now is live and it works with, and it works already with a bunch of like other methods.
[11:15] The methods that we support right now are on Temple, which supports both one-time charge payments and sessions, which we should talk about in a second.
[11:24] We support Stripe, where the interesting thing on Stripe, and Brendan used to be at Stripe, so he can say more about how that works, that it works with anything that Stripe supports.
[11:33] So we could be doing Klarna over MPP to do payments.
[11:37] It supports Visa cards.
[11:39] So Visa wrote an extension to MPP.
[11:41] And we also have Bitcoin Lightning support, which I think is just remarkable that we spoke to the Spark team.
[11:49] We just gave them the spec and same day or the next day, they had proof of concept repository extension to spec, just one shot.
[11:58] Of course, their agents did a lot of work.
[12:00] But I think that was just remarkable.
[12:01] And it just showed how easy this thing is to extend.
[12:04] So may the best standard win.
[12:06] I guess that's where we are right now.
[12:07] Can MPP be exported to other chains besides Tempo, other EVM chains?
[12:12] Absolutely.
[12:13] And again, we just didn't have time to do, you know, integration games are just so hard because somebody will always say, hey, you didn't do my integration.
[12:21] So of course, yes, it can.
[12:23] And we want to do it.
[12:24] I actually think I have a pull request draft up about that.
[12:28] Or maybe it's a thread in our agent.
[12:30] But yeah, it works because it's just call API, get response back, respond back with a signed transaction.
[12:37] This works everywhere.
[12:38] The thing that works nicer on Tempo is that you can pay fees in any stable coin, for example, without having to do more work just because the chain supports it natively.
[12:48] But yeah, of course, it works anywhere because what is an agentic payment?
[12:54] Just a signed payload that says, hey, transfer five bucks to Ryan.
[12:59] Absolutely, it works anywhere.
[13:01] And even the sessions things that we're going to talk about in a second also works anywhere.
[13:05] So because it's just a smart contract that can be deployed anywhere and we've known how to do these things for many years.
[13:10] So yeah, it can be deployed on any chain.
[13:12] It can be deployed on EVM, SVM, whatever you want.
[13:16] We started with the Tempo transactions because that's what we're working on.
[13:20] We're not going to do everyone's integration work up front, but we do want to expand it to more things.
[13:25] So whoever wants to work with us, feel free.
[13:29] Markets are reacting to a world that feels anything but stable.
[13:32] Inflation is sticky, geopolitical risk is rising, and capital is moving between crypto, commodities, equities, and currencies faster than ever.
[13:38] A universal exchange like BitGet is built for this kind of environment.
[13:42] With a major app upgrade, BitGet now gives TradFi its own dedicated tab in the navigation.
[13:46] One click gives you access to stocks, gold, forex, and other global markets, all inside the same platform you already use for crypto.
[13:53] You can get 90% off trading fees on stock perps, and you can trade gold and silver without the fee burn.
[13:57] One app, one account.
[13:59] Trade crypto and traditional assets side by side without bouncing between platforms.
[14:03] No scattered tools, no login juggling, just a unified trading experience built for speed and flexibility.
[14:08] When gold is reacting to global risk, crypto is moving on liquidity, and macro headlines can shift markets overnight.
[14:14] You need a platform that keeps everything in one place.
[14:16] This is BitGet's universal exchange vision in action.
[14:20] If you're the kind of trader who adapts as the world changes, BitGet is built for you.
[14:24] Start trading crypto and TradFi in one place.
[14:26] Click the link in the show notes.
[14:27] This is not investment advice.
[14:28] Galaxy operates where digital assets and next-generation infrastructure come together, serving institutions end-to-end.
[14:34] On the market side, Galaxy is a leading institutional platform, providing access to spot, derivatives, structured products, DeFi lending, investment banking, and financing.
[14:42] With more than 1,600 trading counterparties, Galaxy helps institutions navigate every phase of the market cycle.
[14:47] The platform also supports long-term allocators through actively managed strategies and institutional-grade staking and blockchain infrastructure.
[14:54] That scale is real.
[14:55] Galaxy has over $12 billion in assets on the platform and averaged a $1.8 billion loan book in late 2025, reflecting deep trust across the ecosystem.
[15:04] Beyond digital assets, Galaxy is also building infrastructure for an AI-powered future.
[15:08] Its Helios Data Center campus is purpose-built for AI and high-performance computing, with more than 1.6 gigawatts of approved power capacity, making it one of the largest sites of its kind.
[15:18] From global markets to AI-ready data centers, Galaxy is serving the digital asset ecosystem end-to-end.
[15:24] Explore Galaxy at galaxy.com slash bankless or click the link in the show notes.
[15:27] Giorgio, so I get a sense of urgency with some of just the way that you're talking.
[15:33] I mean, you're in San Francisco.
[15:34] It's the epicenter, the ground zero of what kind of seems like the AI arms race, at least on the United States side of things, the domestic side of things.
[15:42] And I think maybe when we look back, the transition from 2025 to 2026 will be remembered as the time in which society went from chatting with their AI as a chatbot to chatting with their AI as an agent.
[15:55] Like, you know, the agentic word is like a huge buzzword these days.
[15:59] And we're just kind of imbuing our agents with capabilities as we develop them.
[16:05] Like, you know, agents got memory recently and like the MCP protocol was issued and that was like communications.
[16:13] And like with the whole agentic commerce side of things, both X402 and MPP, the standards that you guys are issuing, this is like the tool that we were adding to the agentic tool belt is like, you guys can pay for things now.
[16:24] This is like, you guys now have money and you guys have a native way of paying for stuff on the internet.
[16:31] Sell things, not just paying.
[16:32] And also receive money too.
[16:34] Yeah, like send and receive.
[16:35] Can you just kind of illuminate, illustrate, expand on just like the agentic commerce side of this story, which is the thing that I think the AI arms race is really focused on right now is like trying to unlock that part of the agent tech tree.
[16:52] When we do unlock that, which is seemingly being unlocked, what comes out of that?
[16:58] Like how big of a deal is like agentic commerce broadly in your mind?
[17:02] I think it's huge.
[17:03] Why?
[17:04] So think about it.
[17:07] Like I use my agent to do things more than I click around in Chrome, Brave, whatever.
[17:14] That in itself means that I want to make bookings.
[17:19] I want to buy things.
[17:21] I want to do, you know, all sorts of web crawling off into various services.
[17:26] Like people in our Slack, they want to use, for example, 11 labs.
[17:29] But to them, even the friction of like going to log into the service and like get, you know, billing set up, it's kind of painful.
[17:37] They just don't have, you know, the attention span or the patience to like try out new things.
[17:42] Why?
[17:42] Because we're just in a world where like, we move fast.
[17:44] The world moves fast these days.
[17:46] Yeah.
[17:47] And so people just have low patience to do things.
[17:50] And so while they're trained now to be doing things in their agents, what this means is that they want their agents to be equipped with money and such that their agents can then go and do payments on the web for that.
[18:01] So for sure, I think this makes sense from the user side.
[18:05] Now from the seller side, and I think David O'Ryan, you guys interacted with like this Ben Thompson blog that I shared the other day.
[18:13] Stratechery.
[18:14] Yeah, where the insight there for the seller side is that basically as a seller, your website has to become an API ASAP, not just a UI.
[18:27] Why?
[18:28] Because you want it to be served to the agent in the best way possible such that they go and buy things from you.
[18:34] Why?
[18:35] Because the user isn't going to like go and click around.
[18:37] It's going to be a machine making payments to another machine, hence the name.
[18:42] And so in these cases, like Ben makes a very interesting case about ads, which I don't know if that will play out or not because there's many ways this can play out.
[18:50] But he says, hey, if like way less people are browsing the web with their eyes, then way less people are going to be converting from ads.
[18:56] And maybe that means that this forces all of the sellers or of the people running websites to actually switch to paid APIs.
[19:04] Why?
[19:05] Because, well, they need to monetize somehow.
[19:08] This is already the case, by the way, on Cloudflare where Cloudflare is adding like methods on their endpoints to like fend off the bots.
[19:16] I think there's something more beautiful here, which could be, hey, just embrace the bots, just browsing and like dosing the web and just say, hey, to get through this, just pay me.
[19:26] And so I think there's just like such a strong tailwind to agentic payments that just wasn't there, frankly, last year, where just give five bucks to your agent.
[19:37] And we showed that in the demo that we did with Brendan in our launch video where we gave our agent some bucks, we called it search, gender, image, upload, send email.
[19:46] I've never myself used any of these services alone, but because it could, you know, just crawl the web of services, it could then go and do a multi-step paid workflow
[19:57] across everything, almost like a map reduce or a waterfall, however you want to visualize it.
[20:01] And then that's beautiful.
[20:02] You just give your machine money and it can do amazing things that you never thought were possible.
[20:07] For people who aren't familiar maybe with that Stratechery article, I'm wondering if you guys could summarize that.
[20:13] I know, David, you sent it to me earlier this week and you said, this is one of your favorite articles in Georgios.
[20:18] You just tweeted it out.
[20:19] I just skimmed it and it's called The Agenic Web and Original Sin.
[20:23] We'll include it in the link in the show notes.
[20:25] In my retelling of it, and you guys tell me if I left something off, it's basically back to Marc Andreessen's idea that the internet as we created it and he was there in the early days of Netscape
[20:37] and Mosaic and the internet had this original sin, which is we didn't have a payment standard, you know, a 402 type of standard that was left blank and we didn't work with credit card companies
[20:47] effectively anyway.
[20:48] And because of this original sin, the entire model for the internet was an ad-based model that we still have today, that we still maybe suffer through today.
[20:58] I think Ben was talking about that and saying, well, you know, it had to be that way because with the human web that like the most logical business model was always going to be ad-based anyway.
[21:10] So it wasn't just because you forgot to add a standard, it was just always destined to be this way.
[21:15] But he's saying that the agentic web has, I think, I think what he's saying is it has the potential to completely re-architect the business model of the internet.
[21:27] And so if there's argument is that the sin is now.
[21:30] It wasn't then, but if we don't do the payment things now, that's the sin.
[21:35] The sin is modern.
[21:36] But he's also saying, I think the agentic web will drive a different business model in that AIs scanning different websites, they're not going to click in on banner ads.
[21:46] Yeah, they're not going to be distracted by ads.
[21:47] They're not going to be persuaded or be distracted, okay?
[21:49] But they will want good content and we need good content.
[21:52] We need an incentive mechanism for good content.
[21:56] And so the natural business model that falls out from that is AI agents paying for data providers, paying for content, creating an incentivization mechanism.
[22:05] So the new web actually is kind of this AI agentic web where AI agents are paying directly for content and it's no longer ad funded and maybe the human web
[22:18] just kind of is legacy that's in our past.
[22:22] Is that basically what he's saying?
[22:24] What did I leave out?
[22:24] I think you that was an impressive scheme, Brian.
[22:29] Because that's kind of exactly what he's saying.
[22:33] I think there's a bit of juries out on ads and I'm by no means an ads expert.
[22:38] There's juries out on how ads will evolve on this because you know the whole thesis that ad revenue doesn't convert in the agentic web why?
[22:48] Because agents got no eyes so they don't care about like what number you're on a list or like whether it's surfaced or not because you just
[22:56] tell your agent hey focus on like the actual not on the ads kind of like a native ad blog kind of thing.
[23:02] I think juries out why?
[23:04] Because ads may evolve into prompt injection style things where hey you have the website and the ad is you know text on the website
[23:14] prompt injects it so it could go anyway so I mean also the jury is out too in that the some of the AI companies seem to be looking at advertising
[23:23] as a way to monetize and as a way to grow you know most of the open AI is very much leaning in this direction
[23:30] whereas maybe Anthropic is saying hey no ads that's our special feature.
[23:34] I don't know if you guys agree with this but let me throw out a statement that it would be a much healthier future for the
[23:42] agentic web and for the next internet to be and all of AI to be payments funded rather than
[23:52] ad funded and here's why I say that because I get very worried about a super intelligent force
[24:00] I'm telling all of my life's problems to knows me better than I know myself
[24:05] and has a super ability to glaze me and persuade
[24:09] me to do things I worry about that super intelligent agent
[24:14] who's my best friend being able to upsell me things all of the time and basically
[24:19] manipulate me into whatever it wants to do including buying all sorts of things maybe
[24:25] I don't need I get very worried about that model and so it's more comforting
[24:30] to me to look at a model where it's actually paying for things
[24:35] I know what's going on in the background so I
[24:37] would contend that world is a better world and something
[24:39] that we actually want I don't know if you guys agree with that but that's
[24:43] where I arrived have you seen the Black Mirror episode where they have like a Neuralink style chip on a person's brain in a freemium model and then suddenly no I haven't seen this it's a crazy it really reframes your thinking on
[24:55] you know a lot of things yeah the idea is that you have a chip on your head and in the freemium model every now and then you say something that's an ad to your if you pay you don't have ads so that's great so I think that's a fair statement what you're saying
[25:12] I think people want to feel safety when when telling people their secrets right and it's true that people use the agent or the chat GPT or whatever interface
[25:25] as a more trusted confidator that you know the Google search bar or maybe you know the Google search bar of course itself is evolving and so yeah I think that's a fair statement
[25:35] but again I think it's too early to tell how things will evolve and the best thing we can do right now is observe understand and try to have a notion of preparedness but as David said and absolutely
[25:46] we're in San Francisco things are crazy things are moving really fast and it's hard to make predictions about things you know even a year out from now it's really hard
[25:57] to make predictions and I think the people that can adapt the fastest are the ones that are going to be the most prepared yeah this next part also came from the Stratechery article
[26:08] but George Yost you said it's hard to make predictions but it's easy to spot the trends as you just said people really trust their
[26:17] chat GPT interface or their Claude interface the things that come out of that the text that I read I'm like generally trusting of and I either I realize
[26:26] that oh I typed the wrong prompt or I can actually realize that like this is actually a hallucination but like it's intuitive to me either way
[26:34] so like I trust I trust these websites much more than I do when I go and I see like a Facebook ad for example now there's there's
[26:41] two other technologies that are very related to this there's MCP the model context protocol produced by Anthropic and this this protocol is basically
[26:52] just how agents talk to services once it allows an agent to basically read a website and then there's also NL web this one came from Microsoft
[27:02] and excuse me this is the one where agents can like read a website MCP is communication and so like NL web from Microsoft
[27:12] is like the agent's eyes MCP is the communication between agents so this is all agent to agent stuff or like a native internet to an agent
[27:21] and vice versa and now with MMP or X402 now we also have pay now we just had Ilya from NIR on the show he's one of the
[27:30] also one of the authors of the the Transformer paper and he said his one is one of his early predictions is that you know in the future you're just never
[27:38] gonna go to a website ever again there is no more internet actually like the websites are gone you're just going to talk to your AI in the same way that
[27:48] who's the name of Iron Man what's the Iron Man guy Tony Stark Tony Stark the same way Tony Stark talks to Jarvis and there's no more internet anymore
[27:57] and I can see well that is the internet that is the internet yeah the internet's in the background and I can see the interface changes right and you could easily imagine building
[28:07] a browser right now that actually doesn't care about the JavaScript DOM I think Brenna I forget if I told you about this crazy idea like we could build
[28:15] like a browser that just doesn't care about rendering the web in the proper way you know people say web browsers are really hard build wide because you support
[28:23] all the JavaScript basically all of the whole web you know gigantic test suite but what if you just didn't and just said hey give me raw HTML back
[28:33] so you don't even need the browser the interface is no longer the browser you just don't interpret even the raw HTML and you just tell the agent hey parse this
[28:41] into like a interface that I would like and then you get you know maybe you're Tony Stark or maybe you're Tom Cruise in Minority Report doing things
[28:51] yeah we view and we really intentionally designed MPP as a composable standard that works well with a lot of other things I think you've seen this today
[29:03] where you can plug MPP yes it works in the standard HTTP request flow but it also works in MCP it works over
[29:13] JSON RPC and so you can do all these various transports but we think what the things that people are really
[29:20] excited about next and what we often developers is like okay how do I translate identity
[29:26] how do I translate things like reputation how do you track that across and we don't
[29:34] intend MPP intentionally designed it where we're not going to try and jam all these things together
[29:40] we want to compose with just as we compose with multiple different payment methods
[29:47] by design we're going to compose with multiple components of what are other things that people
[29:53] and machines need to do and are useful so we see a bunch of identity proliferation there's a lot
[30:01] of different standards for discovery etc and we want to work with as many of those as possible
[30:07] and that's why we designed the protocol to be simple as possible and as neutral as possible because it
[30:13] just it's a massive challenge for its juniors very nice too humble to share this but
[30:17] he's also written a great discovery proposal for MPP co-authored with the Merit Systems team
[30:24] which are good friends of ours and we're with them very closely and the idea is that every MPP service can define
[30:30] its schema via again very well owned literally there's a dot well known path that is a
[30:37] well established web standard thing to be discovered by services we're not building a search engine ourselves
[30:43] but we're just building the ways for people to plug into their own search engines the MPP
[30:48] libraries they support MCP or you can just call them over standard rest so again
[30:54] it's not prescriptive about these things these are just layers on top and there's other things
[31:00] for example there's UCP I forget the acronym by Shopify there's A2A by Google there's
[31:07] AP2 there's a bunch of things and they all do different things but none of them really nails the pay
[31:15] angle so we've made it so that you can do the payments based on the things that we talked about
[31:20] earlier and then you can compose it however you want with whatever is on top what I hear there
[31:26] is that you guys don't have an opinion about the direction of the internet if the Ben
[31:31] Thompson Ilya outcome of just like you know there's just your AI and it
[31:37] renders the internet for you to visually appeal to how you like it maybe that's
[31:41] great maybe natural forces point us that way maybe the MPP or agentic
[31:47] payments is like a very important puzzle piece to get us there but
[31:50] you guys are unopinionated about where it goes after this I think it's hard to draw a specific
[31:55] long-term bet I think when we look at the structural trends is there is just going
[32:01] to be more things you see on GitHub more code being generated than ever before there are more
[32:07] services going live on Stripe than ever before there are more people just building things and
[32:13] building things that produce valuable work and we think that
[32:18] those things should accrue value because they're providing value so
[32:22] that's really the purpose of payments you just think there's going
[32:25] to be more things they're going to get built faster and
[32:30] that very much is why we're excited about Tempo and especially machine
[32:35] payments on Tempo is because it draws to the natural conclusion of like okay what is
[32:39] the fastest way to get started today as a developer spin up a service
[32:44] start monetizing it and provide value and get discovered we
[32:48] think that is MPP and specifically MPP on Tempo today because
[32:53] you don't need to touch a single API key this this is really
[32:57] the dream of stable coins of crypto is I just
[33:01] been up a website integrate MPP host it and start getting payments
[33:07] in stable coins immediately and not have to go through large set up
[33:12] flows you only need to do that for offering deeper integrations which
[33:17] we're really excited about so we just want to see
[33:19] more things in the world different ways to monetize and
[33:22] we've been super excited to see new famous developers in
[33:25] that vaulting so the interesting thing about MPP then is
[33:27] that it's great from the least sci-fi to the most
[33:31] sci-fi scenario the least sci-fi being just a paid API
[33:34] the most sci-fi being you know open close run the
[33:39] internet and they all have wallets actually there's millions of
[33:43] open closing like so many of them they all just
[33:45] like non-stop pay each other and there's a lot of like
[33:47] in between stuff that is exciting which is all of
[33:50] the you know the agents crawling the web and paying
[33:53] for services and I think we're not in the least
[33:56] sci-fi I think we're definitely in like a bit sci-fi world
[33:59] based again on the AI tailwinds that we're experiencing and
[34:02] I think the very sci-fi go create a wallet and
[34:16] so I kind of expected to go see okay there's
[34:18] a wallet maybe Tempo is rolled at its own wallet
[34:22] or maybe there's a link to like whatever Metamask or Phantom
[34:25] wallet or everything I'm used to that's not what happens
[34:27] here what happens here instead is I'm greeted with a
[34:31] page that says supercharge your agent it's almost like about
[34:35] spinning up a wallet for my agent instead and there's
[34:39] a button I could click called try with your agent
[34:42] I'm not sure what that does I haven't tried that
[34:44] out but if it's going to connect into my my
[34:45] cloud or my open AI or what but you know
[34:48] the way to use this is kind of like it's
[34:51] a chat type interface find me a hotel and flight
[34:54] to a conference in New York December 28th to 29th
[34:57] no red eyes keep it under $700 right that's the
[35:00] example that you're supposed to send to your agent and
[35:03] I guess it gets a wallet it spins it up
[35:05] and it does this work and it pays for things
[35:08] so even your onboarding flow is like agentic right absolutely
[35:12] so Ryan the thing that so we've sent this demo
[35:16] flow to a lot of people and they all get
[35:17] this wow moment so yesterday we actually told one of
[35:20] our colleagues hey install the tempo skill so every agent
[35:24] agents now have a thing called skills right where the
[35:27] skills are just prompts for how to use the thing
[35:30] so we literally told one of our colleagues to say
[35:33] hey tell your open clue on telegram tell it hey
[35:37] install the tempo skill and call Georgius' number call Georgius'
[35:42] number yeah and like we gave it my number like your phone number I kid
[35:48] you not it called me why did you want this what did it
[35:52] say like to like see what's going on okay like insane
[35:56] to see that hey like somebody literally just gave it a
[36:01] prompt yeah nothing about tempo it literally so the thing
[36:04] that you said like that you read from the website
[36:06] it so we don't have that interface I don't think we'll
[36:11] like I doubt that we would do one sure so just copy
[36:15] that problem you put it in your agent your agent could be amp,
[36:17] cloud, codex, openclow whatever you want yeah it will install the tempo skill
[36:23] it will download the tempo wallet in the background without you even knowing about
[36:27] it it will create a wallet it will tell you
[36:30] to fund it where you can fund it with Apple
[36:32] pay with cross chain deposits from any chain with a
[36:36] QR code flow or with a referral code so afterwards
[36:40] I can just send you a five or more dollar to
[36:43] play around and it just goes then and says hey
[36:47] what services do I have available and then just does
[36:50] it on its own it's really magical it gives you
[36:53] an incredible so when this open claw instance was calling
[36:56] you did it have to go pay for something in
[36:58] order to call you did it pay for a service
[37:01] that we have integrated which lets you do text to
[37:05] speech voice over IP type call or text to speech
[37:10] type thing okay cool where are that when it's setting
[37:13] up the wallet where are the private keys are they
[37:15] somewhere on my machine great so the thing that we've
[37:19] done in wallet is pretty novel I think and it
[37:24] deserves a good explanation which is when you create the
[37:29] temple wallet it kicks you to the website the website
[37:32] that you were just in the website it tells you
[37:35] to face ID to use your iOS biometric auth to
[37:39] create a wallet now once that wallet is created it's
[37:43] using your phone's secure enclave which means that that is
[37:47] not stored on your phone or desktop which is a
[37:53] well established technology for doing this thing it creates the
[37:57] wallet or you sign back into your wallet so there's
[37:59] never a private key in this case but when you
[38:02] call into it from your agent it authorizes it creates
[38:06] an call it ephemeral private key call it a scoped access key
[38:10] that's the naming that we use it generates a small
[38:14] private key that can only access up to a certain
[38:16] number of your funds so if your wallet has say
[38:18] 100 bucks when you log in and when you do
[38:21] the flow it takes you to the website and it
[38:23] says hey authorize your agent to spend up to 10
[38:26] bucks or 10 bucks a day or whatever granularity you
[38:30] want to do which is by the way the same
[38:32] primitive that we use to support subscriptions in MPP so
[38:37] your agent locally gets a private key that's safe to
[38:41] lose which is very useful here it means that if
[38:45] you lose that private key you're covered and if somebody
[38:47] steals that private key the losses are capped which is
[38:51] very useful if you think about hey I just want
[38:53] to let my agent rip but my wallet has $5,000
[38:57] like I don't want it to go and lose all
[39:06] it authorizes it and then you can let your agent
[39:08] rip while feeling safe so is it accurate to say
[39:11] that the master private key right not the sub kind
[39:14] of pass key or private key that the agent gets
[39:17] the master private key is like that's passcode secure enclave
[39:21] on my phone or does it exist do you guys have
[39:24] a copy is it shared at all like a copy
[39:27] of it it's a self custodial wallet it doesn't use any
[39:32] third party it uses passkeys which let you so in
[39:35] tempo we have added the native passkey type if you
[39:38] have seen all of the account abstraction wallets in the
[39:41] Ethereum world they all have this feature but it always
[39:44] requires an extra component called a bundler a relayer whatever
[39:48] you want to call it versus in tempo we pulled
[39:50] that in the tempo transaction format which we have published
[39:54] about which means that you can use passkeys without an
[39:58] intermediary to go and transact with the chain and this passkey
[40:03] is stored on your device and it's also if you're
[40:06] using iCloud keychain or if you're using 1 password you can
[40:10] also sync it across devices okay cool all right now I feel
[40:13] like we need to go back to Tempo and the
[40:20] listeners may be somewhat familiar but I think we need
[40:24] a refresh so this is what this is a layer
[40:28] one it is EVM I think I'm sure the RETH client
[40:32] is involved somewhere Georgios knowing you can you just lay
[40:36] out the specs of this thing and what it is
[40:40] and kind of throughput what assets are on it just
[40:46] kind of some of the details that somebody from the
[40:49] crypto world would want to know Tempo is a layer
[40:51] one blockchain focused on payments we're making opinionated trade-offs to
[40:56] optimize for the payments use case Tempo is permissionless meaning
[41:01] that anybody can run a node and anybody can validate
[41:04] the state transitions of the chain Tempo is live with
[41:09] 11 validators most are operated right now by Tempo and
[41:14] we have some externals running and we're onboarding more validators
[41:19] on this in the next few weeks externals from a
[41:22] geo distributed cluster so that we have in Europe US and so on
[41:26] you're it's permissionless to run a node but you are onboarding more validators
[41:31] how do you square those two things it's it's permissionless to run imagine
[41:35] that you're alchemy for example you can just run a node
[41:39] and like serve RPC traffic or you're an indexer like
[41:43] Album and you want to like index the chain or just
[41:45] a normal cypherpunk user that wants to not trust and
[41:49] verify everything running a node is a two command process so
[41:53] everyone has listen the ability to listen to Tempo but
[41:58] not everyone has the ability to write to Tempo is
[42:00] that correct no it's similar to in ethereum like to
[42:05] become a validator you need to stake 32 ETH right
[42:07] um we don't have that and everything else is the
[42:11] same it means that anybody can run a normal node
[42:15] anybody can submit transactions anybody can create a wallet there's
[42:19] no special case no blacklists anywhere but running a validator
[42:23] is still permissioned in Tempo running while there's still permission
[42:26] we're in the early days we're still figuring out what the
[42:29] right way to expand this validator set is I think
[42:33] we have a pretty promising roadmap in the next few
[42:36] weeks but we need to be very thoughtful about how
[42:39] to execute on this and there's 11 right now validators
[42:41] that are running right now there's 11 and we don't
[42:43] have a dashboard yet on the blog explorer we need
[42:45] to make that happen but there's a validator manager contract
[42:49] in the blockchain that you can check from our docs
[42:52] which if you query gives you the full list and
[42:55] do the validators have to stake something or they're just
[42:58] kind of white listed we have a multi that controls
[43:02] who the validators are okay okay all right so please continue
[43:06] then we were just you know what else should we
[43:09] know yeah so the node is built on the Reth
[43:14] client where the Reth client is a project that we
[43:17] been building at Paradigm for the last four years at
[43:21] this point or more where Reth is built as an
[43:25] extensible client which for validators for MEV bots and all
[43:41] of that it also supports layer 2's like base for
[43:45] example which is running Reth underneath or the rest of
[43:50] the L2 ecosystem and we're also building tempo with Reth
[43:52] why are we doing that because we have a stable
[43:55] foundation which means that we have all of the EVM
[43:59] JSON RPC developer tools they you weeks or month plus
[44:10] something on Ethereum L1 and it's generally very fast very
[44:14] stable well tested it just made sense for us to
[44:17] use that as our foundation so that's on the execution
[44:20] layer side the node has features for payments for example
[44:25] we have a precompile that's an ERC20 contract with permissions
[44:31] enabled in it where if you're a which is generally targeted
[44:35] at stable coin that want to have say various rules
[44:41] or let's say your tether or usdc and you want
[44:43] to instead of like rebuilding all of the permissioning features
[44:46] from scotch we'll just have them available out of the
[44:47] box then node also features a thing called the payment
[44:52] lane where the payment lane is something very valuable for
[44:55] example if you remember late last year when one of
[44:58] the big market volatility and the idea is that you
[45:09] don't want DeFi related spikes to be affecting your normal
[45:14] payment activity so what we do we just said there's
[45:17] a zone there's a part of the block that's reserved only
[45:21] for payments transactions and there's a part of the block that's
[45:23] allowed for anything and the payments section of the block
[45:26] is going to always have predictable stable fees that you're
[45:30] not going to feel anxious about the rest of the block
[45:34] the things that we're familiar with and a big shout
[45:37] out to the commonware team by Pat Grady and Tempo
[45:42] is basically combining the best of the Rath project on the
[45:46] execution side and the best of commonware consensus on the
[45:50] consensus side which is what lets us then execute this
[45:53] ambitious global validator set roadmap that we're going to be executing
[45:58] in the next transactions per second and also validator node
[46:05] requirements to run these things yeah so for gas per
[46:09] block I believe is 500,000 so half giga gas per
[46:14] block and then block time floats from 400 to 600
[46:20] milliseconds it depends on networking conditions at any given time okay
[46:25] and so half a gig of gas does that translate
[46:27] to something like you know 5,000 transactions per second or
[46:33] are we even able to translate does that distinction not matter
[46:38] call it 10 in our last benchmark that was what we could hit so call that
[46:48] like as of last week I believe that's what our last benchmark the thing we're going to be publishing
[46:53] a bench or perf dot tempo dot xyz because I think the hard
[46:58] thing about benchmarks is that you know we're going to talk about them and then in two
[47:02] weeks they're going to be outdated because in the background we have an agent
[47:06] that just looks at all of our stuff and like it continuously optimizes them as
[47:10] you know it's crazy it works like we just have like an agent that looks runs
[47:15] benchmarks all the time and in part that's why the Reth client
[47:19] got so much faster in the last like month and a
[47:21] half wow yeah it's it's really remarkable so David you were
[47:26] saying again much earlier about urgency performance all of that like
[47:29] the AI has really transformed how we work on all of this stuff
[47:33] so really fast block times as you said you said
[47:36] 400 milliseconds really fast block times finality single slot because
[47:42] we use simple consensus half a gigas throughput or sorry half a
[47:49] gigas per block which translates to if you count like
[47:52] 100,000 gas per transaction like you can do the math and
[47:57] then what am I missing network and node requirements well we
[48:02] are actually super excited about this because we because we're
[48:07] building it on RETH and we've been optimizing RETH for
[48:09] the Ethereum L1 use case which is really about like
[48:12] trimming requirements as much as possible we just published a new
[48:17] minimal mode for RETH where Ethereum mainnet itself is 150
[48:21] gigabytes and imagine that Ethereum mainnet has like lots and
[48:25] lots of stuff in it running a tempo node on
[48:30] commodity normal at home software node hardware is possible right now
[48:35] if you open your laptop and you after this and
[48:38] you take say point it to the docs and run
[48:41] me a tempo node I'm promising to you it will
[48:44] work it will download the snapshot the snapshot is tiny
[48:47] right now it will get bigger over time but it
[48:49] will be small because gas pricing or state growth to
[48:53] be good yeah to participate as a validator like is
[48:59] that going to require some beefy bandwidth I think I
[49:01] saw a number of like 10 gigabits per second or
[49:05] something like that is it still primarily if you're participating
[49:08] as a validator let's say or just like running maybe like
[49:11] a serious node are you still going to have to
[49:13] run that in a data center are you guys trying
[49:15] to get this down to like run in your home
[49:18] absolutely not so there's no intention for the again I
[49:24] don't think about validators and non validators different I think
[49:26] it's all the same to me networking wise and node
[49:29] requirements and so on the node operators will require will
[49:37] work on commodity hardware normal residential connection shouldn't need you
[49:41] know gigabits upload in part like why this is going
[49:45] to be possible is because of the common where stack
[49:48] which you know you should like go and look at
[49:50] like what they've done recently where they can use erasure
[49:53] coding to make the networking on a per node basis
[49:56] to be much lighter so yeah like I think it's
[49:59] going to be really exciting I think there's a lot of
[50:01] players that are racing towards bandwidth efficient consensus that's also
[50:06] very high performance big shout out to the team has
[50:09] done amazing work on that with raptor cast I think
[50:12] the world I don't know I think like the world
[50:19] where we thought of you know low block time high
[50:22] throughput and you know again I think like to go
[50:25] to 10,000 TPS everybody or maybe like a bit more like
[50:28] people are covered on a distributed network I think now
[50:32] the interesting thing in the web payments world is like
[50:34] how can we do a million like a billion payments
[50:36] per second things like that and that is like an
[50:39] open question a lot on how people are going to do
[50:41] that our answer is the MPP sessions where you can
[50:44] bypass going to the chain every time but I think
[50:47] that for few tens of thousands of transactions per second
[50:52] like in the next you know even now like I
[50:55] think the world is in a good spot like whether
[50:57] this Tempo Solana Monad like I I'm saying off the top
[51:01] of my head is like the high performance decentralized blockchains
[51:03] I think like people are covered I think the requirements
[51:08] have gone down so much the operator experience has gotten
[51:11] so much better it's been a question I think since
[51:15] Tempo was announced in sort of the crypto circles as
[51:19] to like why an L1 rather than an L2 and
[51:22] I noticed just yesterday you tweeted this Georgios the thing
[51:26] I learned earliest in my crypto journey is that to really
[51:29] scale a decentralized network you have to avoid consensus that's
[51:33] what drove me to L2 scaling you talked a bit more
[51:36] about state channels and L2 this seems to indicate that
[51:41] you're still L2 pilled and yet as one of the
[51:45] architects and engineers on Tempo you guys went with an
[51:50] L1 I think a lot of people are like probably
[51:53] listening to this and scratching their heads and saying why
[51:56] like why an L1 rather than L2 I think the
[52:00] simplest answer is just developer velocity and being able to
[52:04] self express and being able to do the things that
[52:07] we want that's one we didn't want to be bound
[52:10] by the DA that the Ethereum world would provide us
[52:13] at the same time of kind of like be able
[52:23] to self express in all of these ways and I
[52:28] think that's the most of it right I think being
[52:31] able to just own your fate and own your stack
[52:34] and being able to customize as you want is just
[52:37] so important what do you think this means for the
[52:39] L2 roadmap that Ethereum has set off with four years
[52:44] ago is that sort of dead in your mind you
[52:46] think L1s are the way to go or do you
[52:50] think there's a future for L2s I don't think these
[52:53] are intentions so there's two questions here right like A
[52:56] what do I think about L2s in general or maybe
[53:00] for 10.2 what do I think about L2s in the
[53:02] Ethereum context so I can answer the Ethereum context one
[53:07] first and then let me tell world I think these
[53:16] are the best the most credible way to do real
[53:20] scale on Ethereum again even if we make Ethereum scale
[53:24] on L1 we will need to roll some kind of
[53:26] L2 technology in it and it can be done as
[53:30] OP stack arbitrary base all of these things or it
[53:33] can be done in an enshrined way there's this whole
[53:36] native rollups roadmap that that I think L2 are necessary
[53:47] for a decentralized system to scale I think Ethereum has
[53:51] this very cypherpunk core that is important to protect at
[53:55] all costs and I love Vitalik's recent cypherpunk warrior arc
[53:59] I think that's the right thing to be doing so
[54:01] I think for Ethereum absolutely you need L2 and I
[54:04] would definitely not make changes to that I think there's
[54:08] things that in Ethereum world we need to figure out
[54:10] around tensions around branding the whole L2 is competitive to
[54:14] the L1 and all of that people disagree I don't
[54:16] know what the right thing is there but I would
[54:19] absolutely classify L2 as a necessity in the roll-up sense that people
[54:24] have been doing in the temple context I think there's
[54:27] again a few interesting things well A MPP has two ways
[54:33] to interact with one is the charge method the other
[54:36] one is the stream method or the session the charge
[54:40] is every transaction goes on chain which is just a
[54:43] normal payment session or the streaming method is actually opening
[54:48] a one-way payment channel with the server which is like
[54:51] an old school layer two technology from you know before
[54:55] most people heard about a precursor technology to layer twos
[54:59] yeah absolutely it was lightning network like a one hop
[55:07] one direction payment channel just says hey Ryan I'm opening
[55:12] a tab with you instead of settling with you on
[55:16] every query which is a charge method which is how
[55:19] we're used to doing crypto payments write down on your
[55:23] notebook what is my score and then I'm going to
[55:27] settle with you at the end when I want to
[55:29] close out the tab and this means that I can
[55:31] use like an old school layer 2 technology in tempo
[55:35] for the specific use case of client server payments which
[55:39] fits beautifully right yeah I guess like I just want to sink
[55:42] that in that like the layer 2 technology we have
[55:44] we literally just deployed the layer 2 technology this morning
[55:47] on tempo why because even if the chain support whatever
[55:52] many throughput latency constraints their demand that the AI world is
[55:56] going to bring is just 100x that or it's just
[55:59] unknown how much it will scale that it's going to
[56:01] just hit the physical link like to support it you
[56:04] would need 10 gigabits or 100 gigabits of uplink or whatever
[56:07] and we're not I don't think we want to go
[56:10] there yeah I read actually a post on that by
[56:12] Liam Horn who that kind of cypherpunk thing versus what
[56:28] Tempo is doing because as you know Bankless is like
[56:32] primarily a podcast for crypto natives I think for a
[56:35] lot of crypto natives they see Tempo and they have
[56:38] mixed feelings I can say even me going to this
[56:41] episode I have mixed feelings like on the positive side
[56:44] of things it's very exciting to see like obviously a
[56:48] world class engineering team that to the egenic web and
[56:58] kind of winning payments over to blockchain technologies and do
[57:03] see what you're doing with respect to decentralization at the
[57:07] same time for crypto native it's like a lot of our
[57:10] heroes right like Georgios among them originally the loom L2
[57:15] like scaling ethereum Liam Horne who I mentioned Dan Robinson
[57:19] who pioneered you know Uniswap and a lot even even Dankrad
[57:25] this tweeted about tempo right now he's on the tempo
[57:28] team so these are kind of some of the crypto
[57:31] native heroes on this crops type mission right censorship resistance
[57:35] open source private and secure the ethereum track and now
[57:41] they're doing all of this in tempo and some people
[57:45] are scratching their heads and they're saying okay like is
[57:47] tempo now just taking the ethereum vision let's say in
[57:50] this whole cypherpunk vision and corporatizing it or just executing
[57:55] it in a different way and I don't know if
[57:58] they feel kind of like lost by that or they
[58:01] feel like there's a competitive threat or they feel like
[58:05] it's just the open source thing that we once had
[58:09] and the decentralized thing that we once had and the
[58:11] crops thing that we once had now the corporations are
[58:15] here and they're taking over and they're out engineering us
[58:18] and maybe out executing us and so there's some sense
[58:20] of like feeling left behind there I don't know it's
[58:24] a jumble of feelings that I think people are probably
[58:28] having as they're listening to this conversation how do you
[58:32] square these things how do we think about tempo in
[58:34] the context of Ethereum being cypherpunk but maybe now it's
[58:38] a lot smaller than we once thought it would we thought
[58:42] at one time it would take the payment use case
[58:44] and these would be L2s and now it seems like
[58:47] that's happening outside of the Ethereum ecosystem of course you
[58:51] know you're still at RETH you're still co-developing on Ethereum
[58:54] I'm sure that's going to be open source so it's
[58:57] not like Ethereum doesn't benefit and yet it's not benefiting
[59:00] in the same way as we originally thought it would
[59:02] and the question is all of the good stuff that
[59:05] was happening with Ethereum is it going to be happening
[59:08] not on Ethereum and how should we think a question
[59:10] that we like people feel is like why not do
[59:14] all of this on Ethereum right why do this on
[59:18] an L1 chain in tempo with a separate kind of
[59:21] thing separate again look at the niches right like the
[59:31] payments niche just requires so much capacity and so much
[59:36] specialization that and I replied this to someone on Twitter also
[59:40] I think earlier today I think it was Alan who said that are
[59:44] there any approaches that you're doing to precompiles for example
[59:47] which is a technical detail in what we're doing that
[59:50] Ethereum would not do and I'm like yeah of course
[59:53] because Ethereum is a general purpose platform that empowers developers
[59:57] to just self-express in the most general purpose way and doesn't really
[60:00] discriminate for a particular use case which is what makes Ethereum so beautiful at the
[60:05] same time when you're doing the payments use case it's
[60:08] not just the performance stuff there's like all sorts of
[60:11] like specific functionalities that you want to add into the
[60:15] system that just wouldn't happen on Ethereum they just would
[60:18] never go through the governance post it would take too
[60:21] long so that's one point I think the other point
[60:26] is that high value DeFi will continue happening on Ethereum
[60:30] right yeah I guess maybe there's a question which is sort
[60:35] of what you think Tempo's intent is which is is
[60:38] Tempo's intent to kind of eat Ethereum's lunch or is
[60:41] it to sort of expand in a different direction the
[60:46] goal for Tempo is to make the stablecoin native payments
[60:51] world happen and I don't think that's intention with Ethereum
[60:54] being a large successful force for the world to keep
[60:59] going on the thread there's the timing that has happened
[61:04] with the Tempo Maynet launch today timed with the EF
[61:08] mandate document last week there's like a tale of two
[61:11] cities here my read on that document was that Ethereum
[61:15] is like a sanctuary technology to make a sanctuary for
[61:19] people and also not much more than that if the
[61:24] Ethereum broader community wants it to be more than that
[61:26] then the onus is on them to do it but
[61:28] the EF as it relates to that is not interested
[61:34] in doing the agentic commerce agentic payments thing that is
[61:38] going to change the future because it's not about changing
[61:42] the future it's about being a sanctuary for the people
[61:45] that need it the most and there has been just
[61:47] kind of like a shift like with some of the
[61:50] people that Ryan has mentioned like Georgios Donkrad like there's
[61:56] been like a vibe shift of I think people who
[62:00] are interested in growth is maybe something that I will
[62:04] characterize it as like if you were you know previously
[62:07] in the Ethereum camp but you were really into growth
[62:11] economic growth and being more than a sanctuary and doing
[62:16] kind of just like you know whatever is on the
[62:18] technological frontier you know the AI arms race you kind
[62:22] of found your way into the Tempo ecosystem and so
[62:25] there's like while Tempo isn't in tension with Ethereum it
[62:29] does seem to represent a different vibes polarity than Ethereum
[62:34] does that is kind of like equal and opposite and
[62:38] equal there's no question here Georgios I'm just wondering if
[62:40] you agree with the assessment I admit I did not
[62:43] have the time to read the dog I believe it
[62:45] was 30 pages and there's a lot of anime in it my
[62:49] attention span is fried as well and I think there is
[62:55] a fair take around the vision tensions maybe how different
[63:03] visions rally different people I think at the same time I believe
[63:08] in both which is well to me like it has expressed
[63:13] in a weird way where we made Reth a library and
[63:16] any changes that we make tempo faster or make tempo
[63:19] more robust or more feature stable and whatnot it just
[63:23] flows naturally to the Reth upstream library foundry as well so
[63:27] like we announced tempo like one of the core points
[63:29] that we wanted to land on people was that all the
[63:32] work that we're doing yes it's making tempo work but
[63:34] these are the same code bases so the same people
[63:38] that are working on the new code base are also
[63:40] working on the last code base why because they depend
[63:42] on it literally it's like a pain dependency in the
[63:45] code base so that's why to me I don't while I
[63:49] empathize with what Ryan said and I totally understand yeah somebody might feel
[63:54] like hey like some people that were doing good work
[63:56] with our other friends I don't feel that tension as much
[64:02] because we just do both and it might be hard
[64:06] for everyone to understand but we're just doing both from
[64:09] our end and we're good in and we think we
[64:12] can do both very well some exciting news we are
[64:14] launching a new podcast to help people figure out the
[64:17] crypto cycle how to navigate it the best crypto cycle
[64:20] investor I know his name is Michael Nato he runs
[64:22] the DeFi report this is the guy that sent me
[64:24] a sell alert before the 1010 price drop happened his
[64:38] market structure entry targets fair market value of Bitcoin and
[64:42] Ether and where we are in the cycle there's new
[64:44] episodes that are released every Wednesday they're 30 minutes they're
[64:47] short they're punchy I think this crypto cycle is harder
[64:49] to navigate than most so let's do it together go
[64:52] subscribe to this podcast search the DeFi report wherever you
[64:55] get your podcasts YouTube Apple Spotify or find a link in
[64:58] show notes there's a new episode waiting for you now
[65:28] big I think we're very excited like if you look
[65:31] at what we just last said about the future of
[65:34] Ethereum as this extremely decentralized reliable place we think reputation
[65:41] and registry and discovery will live in multiple places and for the most important
[65:47] the most decentralized agents we're really excited about things like
[65:52] 8004 how can you push reputation back how can you say I attest to
[65:57] this thing but we think there's going to be multiple
[65:59] and we don't know how that's going to proliferate so
[66:02] that's why we're really looking at a lot of things we're
[66:05] just trying to see what are people building how do we
[66:07] get the right solution for them and how do we like
[66:28] exactly exactly I think it's very much inequitable and I
[66:31] believe we're Brandon we had that chat with Davide right
[66:33] around one of authors on that where we shared some of
[66:38] our ideas on discovery some thoughts on ERC 8004 and
[66:42] so on so we like the idea we don't know
[66:44] I don't know if it's like the right way to
[66:46] do it yet because people are just going to do
[66:48] things but we're talking to the people about it and
[66:52] we're just giving them our thoughts quick question on assets
[66:55] so what assets are available right now on Tempo and
[66:59] what do you think that will look like say in
[67:00] 12 months from now so there are really two main
[67:03] types of assets on Tempo one is our special stablecoin
[67:09] standard that Georgios talked to called the tip 20 which
[67:12] is an extension of ERC 20 supports a number of things
[67:17] that we just found stablecoin issuers need like policies like
[67:23] controls you can sponsor gas fees it also integrates really well
[67:27] with our stablecoin decks which is an enshrined primitive in
[67:31] Tempo so in a lot of cases and we use this
[67:35] really heavily in MDP if I'm a server I am
[67:39] broadcast service and I want to get paid in USDC
[67:43] but an agent might hold some other currency that's also US
[67:47] data dominated we can handle swaps automatically and do so
[67:52] in a very efficient way that's controlled by the protocol
[67:55] and really just proliferate as many through DIP20 also on top
[68:02] of that anybody Tempo is a permissionless network so you can
[68:06] deploy any token that you want but we have made
[68:11] to George Deuce's point before conscientious engineering decisions so that
[68:15] stable coins via payment lanes via other primitives are more
[68:21] efficient to operate on Tempo than your random run-of-the-mill ERC
[68:26] 20 does that also mean that permissionlessness does that also
[68:29] mean anyone can deploy you know some kind of smart
[68:31] contract outside of a token any kind of defy you
[68:34] know primitive that they want they can deploy that meme
[68:37] coins yeah offensive what about what about offensive meme coins gross disgusting offensive
[68:44] meme coins can I deploy some of already I believe nice David you
[68:51] into those you really into those you inquire how about you mentioned
[68:57] kind of a dex being sort of part of the core protocol in some way has some special
[69:02] status how about identity is there kind of a native identity type engine is
[69:08] everything amlkyc or how are you handling that piece no amlkyc built
[69:14] into the chain itself if you're using chain analysis or whatever else in your
[69:19] app you're free to do so we were considering whether we wanted to add a
[69:24] feature that's not for amlkyc but it's like a co-signer feature on every transaction
[69:29] which the first use case would be fee sponsorship so we already have fee
[69:33] sponsorship natively into the transaction but we're thinking hey maybe we can generalize
[69:38] this in a way that you can do not just fee
[69:40] sponsorship but also security scanning for example like blockade as part as a
[69:46] co-signer or your transaction or if you wanted to add the chain out or
[69:49] something we haven't done that yet so nothing for sure nothing
[69:54] like in the chain around KYC AML it is like
[69:58] app layer concern on a per app basis but we are thinking
[70:02] about hey can we allow people to poke on things
[70:06] more easily to make the app layer better all the
[70:09] existing EVM based smart contracts could those be directly deployed
[70:13] to Tempo and then also kind of the other infrastructure
[70:17] maybe the user infrastructure I mean will Metamask pretty much
[70:20] work with the right RPC out of the box so
[70:25] all of the smart contracts work out of the box
[70:28] there is the FITO so on Metamask there is a
[70:33] well they don't show stable coins as your native balance
[70:38] so that's something that we're working on with the team
[70:41] on okay but all the EVM wallets they will shortly
[70:46] work with Tempo then basically they but sometimes there's edge
[70:52] cases because they're not programmed to show you your stable
[70:56] balance right they're programmed to show your ETH and for
[71:00] example if I have any of the stable coins that
[71:02] we deploy via the stable coin factory that people are
[71:05] using and anybody can interact with anybody can deploy a
[71:08] stable coin and does it by the way it's like it's
[71:12] a we're calling it the stable coin factory but the
[71:15] tip 20 factory is really just a generalized one so
[71:17] it can be for any kind of fungible token so
[71:20] you might deploy something and say it's a stable coin
[71:22] but it might not be backed by anything so treat
[71:26] it as a normal ERC 20 that's precompiled and more
[71:30] efficient has hooks on it but yeah because wallets just
[71:34] don't take all of the stable coins that you have
[71:36] configured and they don't just sum it up and say
[71:38] hey this is your wallet dollar balance they are programmed
[71:42] to show hey what's your ETH balance that's the main
[71:46] thing that we've been trying to make work the other
[71:48] thing is because you're paying fees in any token and
[71:51] Tempo lets you pay from any of your like for
[71:54] example if you're transferring USDC you can pay fees in USDC
[71:58] if you're transferring USDT you can pay fees in USDT and
[72:01] this happens via a baked into the chain primitive the
[72:04] Dan Robinson invented called the fee AMM it means that
[72:08] wallets have needed to do some custom also happening the Ethereum
[72:18] world because as the account abstraction wallets are gaining traction they all basically
[72:24] need to expose that primitive to the wallet and there's some nice
[72:27] ERC standards that we're also following which are basically such
[72:32] that it works the same similar to how the Ethereum world
[72:34] is doing the ERC 437 stuff guys going back to
[72:37] this very big vision of the future of the internet
[72:40] between AI micropayments agentic changing potentially changing potentially critically changing
[72:50] like the idea here is there's going to be like you
[72:55] know trillions of microtransactions being passed around you know any
[72:59] given day money is going to be flying around the
[73:02] internet much faster and it kind of makes me think
[73:05] that we're opening up a opportunity a field of opportunity
[73:09] for brand new types of value to be expressed brand
[73:13] new advice to some young entrepreneur coming out of college
[73:21] he's hungry they're ambitious they want to go do something and
[73:25] they want to catch some of that money that we
[73:27] think is going to be flying around from all these
[73:28] AI agents how would you best steer them in the
[73:33] direction of casting the right net in the right location
[73:36] to catch some of the money that is going to
[73:37] be flying around yeah I think the most efficient thing
[73:39] that we see is figure out like one use the
[73:43] tools a lot and see like okay what are what are
[73:46] they doing where are they getting stuck and wherever you're
[73:49] getting stuck or wherever there's friction we think there is
[73:53] value to be accrued and just build services that unblock
[73:59] developers unblock these machines that are increasingly compounding across every
[74:05] single vertical we see now from code deployment to even just
[74:09] people doing administrative work at their office and figure out
[74:14] where they're going to talk what's the work that they're
[74:15] doing and make that more legible to them and we
[74:19] think value will naturally flow to those services and that's
[74:23] why we really developed MPP we think MPP is the
[74:37] and all these agents are so good at just calling
[74:39] the basic you mix commands that have existed since the
[74:42] 70s and we think the same thing applies where it
[74:47] is extremely intuitive and we found this in testing to call
[74:51] the exact same commands HTTP payment off to perform payments
[74:55] because it is just so baked in and so natural
[74:58] and all the tools exist my take would be just
[75:01] build paid APIs like figure out like for example like
[75:06] David I bet you and Ryan you guys got like
[75:11] a giant corpus of like interesting files with notes you know
[75:16] your prep for all of this like wonderful episodes that you've been doing
[75:19] for so long you could pretty easily just tell your
[75:24] agent hey expose this as a service and instead of like
[75:28] me and Ryan having get queried directly by things why
[75:32] don't these people just talk to my service wait you
[75:35] don't want to come on the show anymore is that a paid
[75:39] service by the way you just you could do it as
[75:42] a paid service you know you get like five three
[75:46] queries and then to go more you know you need
[75:48] to do more I just think there's so many you
[75:52] know of these hey I share the world but I
[76:02] kind of like don't want to put it out there
[76:03] for free or maybe the hosting costs I cannot cover
[76:06] the hosting costs and I don't think about them and
[76:09] like one of our colleagues Shane had said that earlier
[76:11] on which is like you can just build a service
[76:14] that kind of like pays for itself in a very
[76:18] viral article on Twitter a few weeks ago about that as
[76:22] well and in a funny way these are like the
[76:25] self sustaining self building autonomous things where you can just say
[76:29] hey here's some data okay start making money on it
[76:32] when you've made some money on it then you know
[76:34] go build new things with that money and there's actually
[76:37] a very well established concept about that it's called the
[76:39] von Neumann pro which is like the spacecraft goes and
[76:42] builds more versions of itself yeah yeah and so I
[76:45] think like basically the advice that I this thing put
[77:07] in API and it doesn't need to be anything crazy
[77:10] you don't need to like think about it yes can
[77:11] just be like text files Excel spreadsheets templates how you think
[77:15] about the world all of these things so we've got
[77:17] a lot of that we have like seven or eight Google docs
[77:21] that are each respectively like 700 pages long and because
[77:25] these are our notes for our podcast and say we
[77:39] take all the transcripts from the bankless podcast we take
[77:41] all those notes we take everything we've ever produced we
[77:44] clean it up and make it more accessible and that's
[77:50] our value that we've had the corpus of bankless knowledge
[77:53] which is going on for six years now so a lot
[77:55] of value in there about anything we've ever talked about
[77:57] ever how do I tell the agents about it and
[78:02] that it's useful to them and that they should pay
[78:04] me for it how does discovery work well by the
[78:07] way if you you're down to do this we'll happily
[78:10] call install everything we need make it work for you
[78:14] so we can talk about that offline yes yeah but
[78:17] if you wanted to make it like we support a
[78:20] way to discover paid services via MVP today you just
[78:23] say like you register on you can spin up your
[78:26] API and just say hey here are the endpoints you
[78:29] can call this is the cost these are the ways
[78:31] which you can here's the currency I want to be
[78:34] paid in and you can do that not only on
[78:36] tempo but across a variety of payment methods so it
[78:53] like they're calling it like what is like the page
[78:56] rank for productive work and to figure out like okay
[78:59] how do we build that I think that's also part of
[79:03] the question like what's a search engine for agents almost
[79:06] like what's a search engine also how do you price this
[79:09] content it feels like there's a lot I mean do
[79:12] you want ingest like thousands and thousands of lines or do you
[79:23] right and who's going to pay for that it sounds
[79:25] like yeah not very much probably it's like almost like
[79:30] there would need to be a bidding process to discover
[79:32] what the actual market price is here right I'm sure
[79:35] there's a lot to be built in that area we had them
[79:38] so early on so you know how like open AI has
[79:42] like normal pricing and search pricing for the API you
[79:45] can giving 10 APIs you know you said Dan Robinson
[79:56] like that because like this is like exactly the Dan
[79:58] Robinson problem which is like I got 10 queries I'm
[80:02] selling 10 queries you know this is like my data
[80:05] go run an auction figure out the price I can
[80:08] figure out the price that would be valid we haven't
[80:11] done that out of the box yet I think it's
[80:13] a good point the question of the consumer or the
[80:16] person wanting to pay the API is two questions like
[80:19] A how do I price my stuff how does my
[80:22] stuff get discovered I think the answer is either you
[80:27] know what the price of the data is and maybe
[80:29] you charge some premium on it for convenience or whatever
[80:33] else and to the discovery point I think right now
[80:37] what you can do is publish your schema but where
[80:40] do you publish it and what does the search engine
[80:42] look like I think that's open ground right now and
[80:46] I think people are going to race for it if
[80:49] that is the next page round right I think that's
[80:53] going to be beautiful I think there's going to be so many
[80:55] competitors for this rank and hopefully we can just sit
[80:59] below all that and let that competition happen so much
[81:03] to build here guys very exciting the agenic web I
[81:06] think is going to be a pretty big deal and
[81:08] to have you know kind of blockchain crypto be the
[81:10] payments layer for that it just seems like it's got
[81:13] to be the future congrats on mainnet Giorgio Brendan thank you so
[81:17] much for joining us today thank you and you guys Bankless nation gotta let you
[81:21] know of course crypto is risky you