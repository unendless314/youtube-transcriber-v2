---
channel: "Asian Dad Energy"
video_id: "MNI89jIL-7Q"
title: 'Everyone Says AI Is Too Expensive. They''re Wrong.'
published_at: "2026-06-09"
duration: "14:13"
word_count: 10961
---

# Everyone Says AI Is Too Expensive. They're Wrong.

[00:00] Hello, world. I'm an unemployed ex-big tech software engineer with 25 years of experience in the tech industry.
[00:07] So, there was a lot of talk in the news recently about how expensive AI has gotten recently.
[00:12] Due to this drive to use agentic AI for literally everything, many companies are encountering runaway token consumption by their own employees.
[00:21] Individual companies are burning through millions, tens of millions of dollars a month on their AI subscriptions.
[00:29] And some major tech companies have already run out of their AI budgets for the entire year, like right now.
[00:35] I've even heard about an executive at NVIDIA saying that his team had consumed so many AI tokens that AI now effectively costs more than the employees using it, thus making AI more expensive than human labor.
[00:51] Now, I think there are a lot of emotions and vested interests at play here.
[00:57] Some people probably wish for the AI transformation of the economy to succeed, but I suspect there are far more people, probably 10 times as many people, who are secretly rooting for AI to be uneconomical and for the whole venture to fail.
[01:14] And there are naturally a lot of emotions around it, right?
[01:18] We're talking about huge amounts of money, people's jobs, their entire livelihoods, hinge on how this question is answered.
[01:26] So I get it.
[01:27] With that said, however, my humble opinion is that AI technology is already cost effective today, and it's only going to get cheaper in the future.
[01:39] Why is this?
[01:40] Well, there's a number of enabling technologies that are already here today.
[01:45] These technologies have already dramatically lowered the cost of using AI today.
[01:52] They are just not evenly distributed yet.
[01:56] Now, before I jump into the technical weeds here, I just want to mention that these technologies didn't jump out of nowhere.
[02:04] They were developed as a consequence of the geopolitical contest between America and China.
[02:11] So, some quick context.
[02:13] America today, we dominate the global tech ecosystem, right?
[02:20] We directly or indirectly control every rung of this tech ecosystem, from the frontier AI models, to big tech platforms like Google and Amazon and Facebook, to even the semiconductor industry that powers the whole thing underneath.
[02:36] Since everybody on Earth now needs this digital infrastructure just to live and do things, having control over this tech ecosystem gives huge financial and political benefits to the country that controls it.
[02:51] So, obviously, China wants their tech ecosystem to be the top dog here, right?
[02:58] But the seat's already taken.
[02:59] And that's why we got this competition.
[03:02] And, on the surface, a great way for America to win this contest is to strangle China's infant tech industry in the cradle.
[03:12] And we've been trying to do this by strangling China's supply of compute resources.
[03:18] This is done by putting sanctions on the export of powerful computer chips to China, and by sanctioning the export of semiconductor manufacturing equipment.
[03:30] Cutting off the equipment makes it much harder for China to make cutting-edge AI chips themselves.
[03:37] Now, kind of ironically, being so resource-constrained because of the sanctions, it has forced Chinese tech companies out of sheer necessity to come up with a bunch of interesting innovations.
[03:52] Innovations that end up delivering AI models, which are nearly as powerful as the most powerful frontier American models, but at a tiny fraction of the price.
[04:03] So, with this context in mind, let's jump in.
[04:07] So, an AI large language model, it has to be trained with literal crap ton of data.
[04:14] This training process is extremely expensive in terms of compute, energy, and water resources.
[04:21] Take OpenAI, for example.
[04:23] They trained their GPT-4 model for about $100 million.
[04:28] But, if we looked at a contemporary and fairly competitive Chinese model, like the DeepSeq R1, they trained that model for $6 million.
[04:40] One big reason for this giant discrepancy is innovations in the model architecture.
[04:47] Specifically for DeepSeq, they improved the model's underlying transformer architecture.
[04:54] Moving from the standard dense multi-head attention mechanism, or MHA, to a sparse multi-head latent attention mechanism, or MLA.
[05:08] Now, obviously, guys had to do some hard math to figure this out.
[05:13] But, this one algorithmic change, it resulted in a 2x to 5x reduction in the total amount of compute resources needed for training.
[05:25] For the training phase of an AI model, you have to gather a huge amount of data.
[05:30] Then, you have to go through all of these computationally expensive stages.
[05:35] Pre-training, training, post-training, and so on.
[05:39] But, suppose there's already a frontier AI model out there.
[05:44] Some other guy had already done this expensive computational grunt work for you.
[05:50] Well, with model distillation, you can transfer the intelligence of this expensive pre-existing AI model into your own AI model.
[06:02] So, instead of reinventing the wheel, Chinese models like DeepSeq will often use data, output, and behaviors that are distilled from existing American frontier AI models.
[06:17] This accelerates their own training.
[06:19] Distillation cuts model training costs by drastically reducing the amount of data that's needed for training, And, the compute resources required for training.
[06:31] We're talking about a savings of upwards of 75%.
[06:35] So, once an AI model is trained, you can then go and inference that model.
[06:41] Inferencing is when you ask the model a prompt, and the model then takes that prompt and goes through everything that it learned during training to be able to answer that prompt.
[06:53] So, obviously, inferencing will take some compute resources.
[06:57] In fact, that's where a lot of the AI token costs come from.
[07:02] Now, for inferencing, many Chinese AI models have introduced a number of software-based optimization techniques.
[07:11] Optimization techniques like multi-token prediction, mixture of experts, and so on.
[07:19] Let's take mixture of experts, for example.
[07:21] So, this technique breaks down a giant neural network into multiple smaller sub-networks.
[07:30] So, for every incoming piece of prompt data, they built this router that would take this input prompt and route it only to the specific expert sub-network that's needed to do the inferencing.
[07:45] By activating only the part of the neural network that's needed to get the answer, this technique reduces the cost of inferencing by anywhere from 50% to as high as 90%.
[08:00] So far, we've been talking about innovations in software architecture and algorithms and so on.
[08:06] But innovations in computer hardware also matters, right?
[08:10] As I mentioned earlier, America is sanctioning China pretty hard in terms of semiconductor manufacturing equipment.
[08:19] Because of these sanctions, China simply lacks the tools to manufacture the most leading-edge semiconductors for their AI chips, at least not on any reasonable scale.
[08:32] As such, their best locally made AI chips are about two generations behind NVIDIA's most advanced chips in terms of transistor density.
[08:44] So, to compete, Chinese tech companies had to innovate around this blocker.
[08:50] Take, for example, Huawei.
[08:53] They focused on developing application-specific integrated circuits, or ASICs.
[08:59] These are custom-designed chips that are tailored to perform one specific computational function very well.
[09:08] So well that ASICs can sometimes match or even outperform more advanced general-purpose chips like GPUs for that one specific function.
[09:19] So, Huawei developed their Ascend family of AI chips with a focus on inferencing operations.
[09:28] These Ascend chips are made by the Chinese semiconductor company called SMIC.
[09:34] And technologically, they're about two generations behind their NVIDIA counterparts.
[09:40] But if we did an apples-to-apples comparison, for the same amount of compute delivered, an Ascend AI chip would cost a lot less than their NVIDIA counterpart.
[09:53] It would cost less than half as much due to the much older and cheaper chip manufacturing process being used.
[10:02] But when properly networked into a supercluster and used just for AI inferencing operations, these ASIC chips, they actually outperform their NVIDIA counterparts.
[10:16] So, you got all these data centers.
[10:19] They're filled with AI chips, right?
[10:21] And they're doing training and they're doing inferencing.
[10:24] And it's consuming a huge amount of electricity.
[10:27] And electricity is a big part of the AI cost.
[10:31] But what if each kilowatt hour of electricity could cost a lot less?
[10:38] Well, in an apples-to-apples comparison, utility-scale solar panels generate electricity at less than one-third the cost of coal and nuclear power.
[10:52] And China just happens to have the largest production and installation base for solar panels on planet Earth.
[11:00] Because of this, their electricity costs less than half of what it takes in America, further increasing their AI cost advantage.
[11:10] So, because of these innovations, we're now in this situation where the leading Chinese AI models are almost as good as the best frontier American models.
[11:23] But they cost anywhere between one-fifth to less than one-tenth the cost of American AI models.
[11:31] I'm going to be blunt.
[11:32] I've been using ZAI's GLM model pretty regularly over the last couple of months.
[11:39] Now, for the vast majority of my use cases, GLM performs at parity with Claude Opus.
[11:47] But it's doing so for around one-tenth the cost.
[11:50] And here's the thing, though.
[11:52] Nothing really stops American companies from using the same innovations to reduce their AI costs.
[12:00] The reason why American AI companies like OpenAI and Anthropic have not been doing this is because they've been having effectively infinite investor money up to this point.
[12:14] They got so much compute resources at their disposal, it just wasn't worth their trouble to optimize.
[12:22] Now, the macro financial situation may be changing.
[12:25] Now, the investor funding is being questioned.
[12:30] And American AI tech companies need to show profitability at all costs.
[12:36] Maybe the tech industry will sacrifice its own workforce to keep their stock valuations propped up.
[12:43] Maybe this AI bubble will just pop sooner rather than later.
[12:48] Who knows?
[12:49] But in my opinion, the bubble is really just background noise.
[12:54] People, they're just going to keep grifting and scamming.
[12:58] Money is going to be made.
[13:00] Money is going to be lost.
[13:02] It's as predictable as the sun rising and setting every day.
[13:06] But if we can get away from that noise, we can clearly see that the cost of actually using AI, it can and is being dramatically reduced.
[13:18] This reduction is through the use of technologies that already exist today.
[13:23] It's just not being done by American AI companies just yet.
[13:28] So, bottom line, will AI become just too expensive and fail to be adopted?
[13:35] Well, anything is possible, but I wouldn't bet on it.
[13:39] And that's all I have to say about that.
[13:41] Anyways, if you have a morbid curiosity to join me on this life journey, please feel free to subscribe to my channel and subscribe to my Substack newsletter.
[13:52] If you want to support me in my VLOG creation efforts, please feel free to become a member of this channel or just buy me a coffee.
[14:02] If you want a one-on-one coaching session with me, just schedule it.
[14:06] Anyways, thanks so much for watching.
[14:08] Talk soon.
[14:09] Bye.