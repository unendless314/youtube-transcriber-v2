---
channel: "Coin Bureau"
video_id: "xSonLY4u0u4"
title: '$100M DRAINED From Crypto''s Safest Wallet!'
published_at: "2026-08-06"
duration: "16:53"
word_count: 15055
---

# $100M DRAINED From Crypto's Safest Wallet!

[00:00] If you hold your Bitcoin on a hardware wallet because you thought that it meant it's 100% safe, you need to watch this immediately. Over the past few days, attacker scripts have drained more than $100 million in Bitcoin from thousands of cold card wallets, the exact vices recommended by top security experts. So today, we're breaking down the 5-year-old bug that destroyed the gold standard of self-custody, how automated drainers swept 500 wallets in under 25 minutes, and the exact step-by-step emergency protocol that you must follow right now to secure your funds.
[00:34] My name is Louis, and this is the Coin Bureau.
[00:37] Now, let's start with what happened on the night of the 30th of July, 2026. Between roughly 131 and 156 UTC, 594 Bitcoin, around $38 million, left approximately 500 single-signature wallets. Over just 25 minutes, everything we know about self-custody changed. Then, it kept going. The wider sweep that night hit 1,196 addresses for 1,082 Bitcoin, about $70 million, in a 41-minute window. By the 2nd of August, Galaxy Research had it at 4,585 addresses and roughly $89 million. By the 3rd, we're at 1,816 Bitcoin, across somewhere between 5,200 and 7,300 addresses. And Galaxy's Alex Thorne was watching fresh sweeps land in the mempool as he provided real-time updates. The coins that were taken had, on average, sat completely untouched for over three years. These were the people who did everything right, bought the recommended device, wrote the words down, and never touched their wallets again.
[01:53] But there's some important detail here that makes this difference to every hack that we've ever covered on this channel. You see, nobody got phished here, and nobody plugged their device into a dodgy computer.
[02:05] Not one user proved a malicious transaction. The devices were sitting offline, in safes, or hidden away in some corner of the house. One victim, a Canadian entrepreneur called Jonathan Goodman, lost 18.25 Bitcoin, roughly 1.6 million Canadian dollars, from wallets stored in a safety deposit box, drained in a seven-minute window, while the device itself sat in a vault untouched.
[02:31] So, the attack never actually touched the hardware. It went after the software that generated the seed phrase in the first place. Now, to understand how that's even possible, we have to go back to the 1st of March 2021. CoinKite was migrating its firmware over to a new cryptography library called Libingoo. And inside that library, there was one line of code that asked the wrong question.
[02:56] To get a little technical, in C code, you can check two different things about a setting.
[03:01] You can check whether the setting exists, or you can check whether the setting is switched on.
[03:08] Those may sound like the same question, but they are certainly not. Think of it like walking into a room and asking, is there a light switch on the wall? Why, yes, there is. Brilliant. But that tells you nothing about whether the light is actually on. ColdCard's board configuration had a setting called Micropy HW Enable RNG, and CoinKite had deliberately set it to zero, to off, because they were using their own separate hardware randomness wrapper instead. But the library only checked whether the switch existed.
[03:44] So, the code concluded that hardware randomness was handled, and stopped calling the chip's dedicated hardware random number generator. Instead, it fell back to a software substitute buried inside MicroPython called the Yasmerang generator. And that software fallback created the random numbers using the chip's serial number, and the exact timing of when it started up. In simpler terms, that means values an attacker can guess, narrow down, or simply enumerate one by one. And after that initial startup, it never collected any fresh randomness again. Every single output after that was just a calculation from a starting point somebody else could reconstruct. And the reason nobody caught this for over five years? Well, the hardware random number generator was still alive and working elsewhere in the firmware. Internal reviews confirmed it was present and it was configured. Nobody noticed that one code path that actually creates your seed phrase was was walking straight past it. So, five years of devices shipping a downgrade that looked identical to a device
[04:53] working perfectly. Scary stuff. Now, let's look at what the downgrade actually did to your keys, because this is the part that decides whether you're affected. Your seed phrase, those 12 or 24 words written down somewhere, is really just one enormous number picked at random out of a pool. And the whole security model rests on that pool being so absurdly large that guessing your number is next to impossible.
[05:21] The target is 128 bits, or 256 bits for the paranoid. To give you a sense of what 256 bits means, there are not enough atoms in the observable universe to give every possibility its own atom. Not with every computer on earth running until the sun burns out at least.
[05:40] Now, here's what the bug did. On Coldcard's MK2 and MK3 devices, the bug reduced the seed's effective security from 128 bits to roughly 40 bits. The newer MK4, MK5, and Q models still had around 72 bits, because their secure chips added some extra randomness. 40 bits, 40 bits, though, is small enough to simply write down as a list. It's about a trillion possibilities, and that is something an ordinary laptop can grind through offline in hours.
[06:11] Same 24 words on your screen, and the same little OLED display telling you everything is fine, but a completely different universe of difficulty settings behind it.
[06:21] And this is exactly why the drains were automated, and why they were so fast.
[06:26] The attacker didn't really break anything. They didn't need a vulnerability in Bitcoin, and there was no need to even touch your device.
[06:34] They generated every candidate seed in the strunken pool on their own machine, derived the addresses, checked which ones held coins, and then swept them.
[06:45] Kraken's chief security officer, Nick Percoco, noted that the secure element chips in the MK4 and MK5 were properly certified components.
[06:56] But that, quote, nobody verified which code path actually ran.
[07:00] Oh, and there's one more thing that's being underreported in this story.
[07:05] That same broken randomness path wasn't only used for seed phrases.
[07:09] It also fed paper wallet private keys, seed XOR split masks, device cloning keys, USB encryption keys, key teleport temporary keys, and even the web 2FA secrets, and secure notes passwords.
[07:25] So, the blast radius is wider than your main stack.
[07:29] Now, as you could likely tell by now, keeping on top of a story like this is nearly impossible for a single person.
[07:35] It requires a team of people doing research all day to stay ahead of the curve.
[07:40] So, we made things easier for you.
[07:42] Right here on YouTube, you can join the Coin Bureau Club Lite plan for just $10 a month.
[07:48] You get all the important daily market updates across both crypto and traditional finance.
[07:52] Our teams read on where things are going, and none of the noise.
[07:56] Just tap the join button below this video to get started.
[07:59] And now, back to the wallets.
[08:02] Because there is a group of people who came through this completely untouched.
[08:05] And why they survived is one of the most insightful parts of this whole story.
[08:10] Three groups were safe.
[08:12] First, anyone who rolled their own dice during setup.
[08:16] You see, cold cards let you roll physical dice and feed that into your seed.
[08:21] And CoinKite's threshold here is at least 50 fair, independent rolls.
[08:27] If you did that, you injected real-world randomness the firmware could not ruin.
[08:32] Second, anyone using a strong BIP39 passphrase.
[08:36] That's an extra secret word or phrase that you type in on top of your 24 words.
[08:42] And it produces a completely separate wallet.
[08:45] Guessing the weak seed gets an attacker nothing without it.
[08:49] Third, anyone in a genuine multi-sig setup, where you need multiple different keys from multiple different devices to move funds.
[08:57] And this is being shown in the data.
[08:59] As of the 3rd of August, across all four waves, not a single multi-sig wallet had been hit.
[09:05] Not one taproot address either.
[09:08] Which tells you something about how narrowly the attacker's script was scoped.
[09:12] But the important detail is that every single one of those three protections is an optional extra step.
[09:19] Every one of them is the step the setup guide lets you skip.
[09:23] And the people who took those steps didn't do it because they knew about a firmware bug.
[09:28] They did it because they had a healthy amount of paranoia in general.
[09:32] So, the survivors of the largest hardware wallet failure in Bitcoin's history were saved by their security habits.
[09:39] The safety margin came from those extra safeguards that the users added on themselves.
[09:44] While the default setup offered no defense at all.
[09:48] Now, for what it's worth, CoinKai's response has been fast and it has been direct.
[09:52] CEO Rodolfo Novak, NVK, went public almost immediately.
[09:57] His words, I'm sorry, and I'm devastated.
[10:01] Our team is heartbroken about yesterday's news.
[10:04] Then, before any of the technical explanation, he told users, if you generated a seed using a cold card wallet, move your funds now.
[10:13] He took full accountability for the firmware bug.
[10:17] CoinKai halted shipments, destroyed the remaining warehouse inventory carrying vulnerable firmware, and shipped emergency patches.
[10:25] But on that note, I want to cover something very important here.
[10:29] Updating your firmware does not fix the seed that was already generated.
[10:33] The patch stops the device from creating new bad keys, but it cannot unweaken an old one.
[10:39] As CoinKai themselves put it, the weakness follows the recovery phrase itself, not the physical device.
[10:47] So, moving that same seed into a different wallet doesn't help either.
[10:50] If you update and stop there, you're still standing in front of an open door.
[10:55] And one more thing worth knowing about why this wasn't caught faster.
[10:59] CoinKai deliberately purges customer records after 120 days for privacy reasons.
[11:04] So, a data breach couldn't expose the buyers.
[11:07] Which is good in one sense, but it also means that they had no way to email 5 years of customers and warn them.
[11:14] That's a good privacy policy, but the trade-off is a catastrophic notification problem.
[11:20] Now, let's shift our focus a bit.
[11:22] Because if you think that this is an isolated problem for cold card and its customers, then you're mistaken.
[11:28] Randomness is the recurring failure point in the entire crypto industry.
[11:32] And almost nobody audits it, because a bad random number produces no visible symptoms whatsoever.
[11:38] In 2023, there was the milk sad bug.
[11:41] Libitcoin Explorer created wallet seeds using a 32-bit timestamp.
[11:46] That left only around 4.3 billion possible keys, which could be searched on a normal home computer.
[11:52] At least $900,000 was stolen in the first wave, while total losses across several blockchains reached millions.
[12:00] In 2022, the Profanity Vanity Address tool made a similar mistake.
[12:06] It used just 32 bits of randomness instead of 256.
[12:11] That flaw directly led to the $160 million winter mute hack.
[12:16] Researchers later showed that the private key could be cracked on a laptop in under 48 hours.
[12:23] Then, in 2022 and 2023, Trust Wallet's browser extension created keys that could be worked out from nothing more than the wallet's public address.
[12:31] And just a few weeks ago, in July of 2026, Coinspect revealed another similar bug called Ill Bloom.
[12:39] It affected several mobile and browser wallets.
[12:42] And on May 27th, attackers drained 431 accounts in one coordinated attack, stealing around $3.1 million.
[12:51] Total confirmed losses later passed $5 million across five different blockchains.
[12:57] So, here's the big picture.
[12:59] A hack you can see gets fixed within hours.
[13:02] A number that isn't random enough looks absolutely identical to one that is.
[13:07] And it can sit there for five years while you sleep soundly.
[13:11] So then, what do you actually do about it, especially if you hold a cold card device?
[13:16] Well, let's walk you through the practical steps that will keep you safe.
[13:20] Step 1. Check whether your seed was created on firmware version 4.0.0 through version 5.0.3.
[13:29] The creation date is what matters, not what your device is running today.
[13:34] Step 2. Unless you used 50 or more dice rolls, a strong unique passphrase, or a multi-sig, assume that seed is compromised.
[13:44] Step 3. Understand that updating firmware is necessary, but it is not sufficient.
[13:50] Step 4. Generate a completely new wallet on patched firmware.
[13:54] Step 5. Move your funds to the new seed, now.
[13:59] Step 6. Treat the old seed as permanently public.
[14:03] Never reuse it and never fund it again.
[14:07] Step 7. Verify the new receiving address on the device screen before you seed anything meaningful.
[14:14] And one final warning, because the scammers are already circling.
[14:18] Do not, under any circumstances, type your recovery phrase into a, quote, vulnerability checker website.
[14:26] Phishing tools imitating legitimate checkers are already live, so be wary.
[14:32] And so, where does all of this leave us as crypto users?
[14:35] Well, let's first reject one of the lazy conclusions here.
[14:39] This is not an argument for putting your coins back on an exchange, even though that's exactly what happened.
[14:44] Cryptoquant's Julio Marino flagged that daily exchange deposits under 10 BTCs spiked to 7,300 BTC on the 31st of July, the highest since February.
[14:56] Three years ago, FTX taught everybody to pull their Bitcoin off exchanges.
[15:00] This week, a firmware bug seems to be pushing people to do the opposite.
[15:04] But consider what really happened here.
[15:07] Nobody broke into a safe or forced someone to hand over a seed phrase.
[15:11] The attackers simply guessed a predictable starting number.
[15:15] And custodians run on the exact same primitives, with far less transparency and no open repository for anyone to check.
[15:23] The real shift is this.
[15:25] Verifiable self-custody now beats trusted self-custody.
[15:29] Things like those dice rolls, passphrases, and a multi-sig are no longer paranoid overkill.
[15:35] These have become the baseline, because every single survivor in the story was someone who added their own randomness or their own second key.
[15:44] This is an open-source ecosystem that found a 5-year-old flaw in its most trusted device, published it, patched every affected model within days, and had Ledger, Treasure, Bitbox, Foundation, and Blockstream publishing proofs of their own randomness pipelines within days.
[16:03] Nothing in traditional custody works remotely like that.
[16:07] So, the truth is that the people who upgrade their setup this week will end up holding Bitcoin in a way that is harder to break than anything that existed before this bug was found.
[16:16] And that's an encouraging thought.
[16:18] But, what do you think?
[16:21] Does this incident prove that self-custody demands multi-sig as the bare minimum?
[16:25] Or, does it prove that most people were never equipped to hold their own keys in the first place?
[16:30] Please, get highly opinionated in the comments down below, and let us know what you think.
[16:35] And, if you have your security in check, but want to find out how to avoid other mistakes that can cost you money, then check out this video right over here.
[16:43] Thank you all so much for watching, and I'll see you again very soon.
[16:47] Stay safe, and this is Louis, signing off.