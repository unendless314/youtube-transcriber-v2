---
channel: "Asian Dad Energy"
video_id: "M4lqyeA7Vow"
title: 'STOP Paying for Subscriptions — Build This Homelab Instead'
published_at: "2026-04-20"
duration: "24:18"
word_count: 18844
---

# STOP Paying for Subscriptions — Build This Homelab Instead

[00:00] Hello world. I'm an unemployed ex-big tech software engineer with 25 years of experience in the tech industry. Now that I'm involuntarily early retired, I finally got the time to notice a few things about our world. It's becoming clearly apparent to me that a handful of big tech companies have a near total monopoly over our digital lives. This is done through the form of subscription services. We have a dependency on these digital services for working, for entertainment, for even just living our lives. Now, these tech giants have fostered this kind of dependency on their subscription services by making it super easy and cheap initially for people to opt into. But as more and more people become subscribed and dependent on these services, they're then able to jack up the prices while reducing the quality and functionality of these services. A good example of this is Netflix, right? Where they keep raising the price
[01:02] of their monthly subscription and then simultaneously they keep adding more and more ads into their service, disrupting the movies that we're trying to watch. So I don't want to be this dependent on the big tech companies because honestly, I don't like spending so much money on it and it just sucks. And that's where the idea of a home lab comes into play. The idea of a home lab is that of hosting your own hardware and using it to run your own software services in your home network. This then allows you to cut out these subscription services and save yourself lots of money.
[01:43] So how do we create a home lab? Well, I've been running my home lab for several years now and want to share some tips. The first thing you need is hardware. For any home lab build, there are basically three components of hardware to consider. Compute, storage, and networking.
[02:03] Let's take a simple example. Suppose you have a used laptop, right? The compute in this laptop is a chip set. It's CPU and GPU. The storage is the hard drive that's internally attached to this particular laptop. Since this hard drive is directly attached to the laptop and only accessible by that laptop, we call this kind of storage direct attached storage or DAS. And the networking here would just be the laptop's wifi or ethernet connection to your home network. Now, this one laptop is actually enough to create a simple home lab. A single machine that runs all of your home lab services is also called a home server. And just a single home server may actually be good enough for many people. Now, if we think about it, all of those big cloud hyperscalers out there, right, like Amazon Web Services or Microsoft Azure, in their giant data centers, all they're really doing is scaling up this basic concept of compute, storage, and networking. Except they push it to a huge scale. Think tens of thousands of computers, zettabytes of storage,
[03:31] all networked together. Now, we can do a similar form of hardware scaling at home. For compute, we can cluster multiple computers together to form a more powerful compute cluster. We can scale up storage by to get these hard drive bays that allows you to plug in multiple hard drives. Then this bay of hard drives can itself be attached to a computer. And using software, these hard drives would then be exposed to other computers on the network, creating what we call a network attached storage or NAS. Now, on the internet, you can find many diverse examples of people's home lab builds, right?
[04:16] Everything from running your home lab on a single Raspberry Pi to something that looks straight out of an Amazon data center.
[04:28] Now, there are many, many different types of computers that you can use to build your home lab. On the market, there are many really powerful computers with tons of CPUs and GPUs and RAM. But these high-end computers are also insanely expensive right now. Likely due to all the semiconductor supply chain issues that we're seeing across the industry.
[04:53] But you could buy that if money is no issue for you. However, my recommendation is to buy your hardware with the most affordable used hardware when possible.
[05:06] I recommend the following three-step procurement process.
[05:10] Step one is to reuse existing old computers.
[05:14] Suppose you already have a computer or mini PC at home. It's old and you're not using it.
[05:22] That could be a perfect start to a home lab.
[05:25] I have an old Raspberry Pi from a project many years ago that had just been sitting in my drawer for a long time and I decided to use it for my home lab.
[05:35] Step two is to get your equipment from work.
[05:38] Does your job have an IT department?
[05:41] For many corporations, the IT departments would procure large numbers of laptops and mini PCs for their employees, right?
[05:52] And every four to five years, there is a refresh cycle where they would replace these older computers with newer computers.
[06:01] When that refresh cycle happens, the IT department can often get rid of their older equipment for a shockingly low price.
[06:10] For example, I got a few 2010 era laptops and a ton of hard drives from my IT department at work over the years.
[06:21] And I never paid more than $10 to $20 per laptop.
[06:26] The next step is to buy used hardware from online marketplaces like eBay.
[06:32] Now eBay offers sometimes great discount on used old hardware like laptops and mini PCs.
[06:39] Now you may not find a computer for $10, but I've seen many examples of useful computers for under $50.
[06:48] As a bonus, other components on eBay, like CPUs, RAM, disks, and so on are also relatively cheap.
[06:58] So for my home labs, three computers and about four terabytes of storage.
[07:04] I think I must have spent all in around $100 to procure it.
[07:10] Now, once you get your hardware, you want to hook up these computers to a power strip and connect them via Ethernet cable to your network router.
[07:20] Now, specifically with old laptops, their batteries are chemically volatile.
[07:27] And so if we leave them plugged in for long periods of time, like years, there's a fire risk involved.
[07:34] So for me, I remove those batteries from the laptops.
[07:38] Now, my home lab is built with old laptops and a Raspberry Pi.
[07:43] Aside from being super cheap to acquire, it is also remarkably cheap to operate and to maintain.
[07:50] I spent about $5 a month in electricity to run this home lab.
[07:55] And over the last six years, I think I've only had two things break on me.
[08:01] One was a CPU fan and then there was a hard disk that broke.
[08:05] So once you have the hardware, the next step is to install an operating system on your home servers.
[08:11] There are many different kinds of operating systems to choose from.
[08:15] If you have a powerful computer, right, with tons of CPUs and RAM, it might be worth it to install a hypervisor like Proxmox.
[08:25] A hypervisor allows you to create virtual machines like virtual computers that are sitting on top of the underlying physical computer.
[08:38] Each of these virtual machines could have their own operating system.
[08:42] With a hypervisor, you could have one virtual machine running on Windows operating system and another virtual machine running on the Linux operating system, for example.
[08:54] With that said, however, I find the Linux operating system to be the most ideal one for home labbing because it's free, open source, and highly resource efficient.
[09:06] I use the Lubuntu and Raspbian variants of Linux on my home servers.
[09:12] Now, along with the operating system, you might want to consider installing software that will make your storage more resilient.
[09:21] Why do we need that?
[09:23] Well, by default, hard drives run on the standard called RAID 0, okay?
[09:30] And what it means is suppose you have a file that's important to you, like a document or an important photo, and that's stored on your hard drive.
[09:38] When that hard drive dies, that file is gone.
[09:42] Now, if we look at a subscription service like Google Drive, for example, one of its key selling points is that your files will not be lost if a hard drive at Google's cloud data center happens to fail.
[09:58] So, in our home lab, we can achieve that same kind of resiliency to hard disk failure through using software.
[10:08] Software that reformats your home lab's hard drives to be RAID 5.
[10:15] Now, my favorite software tool to do this is the MDADM utility.
[10:20] Now, once we have our operating system installed, it's possible to install our software services directly on that operating system.
[10:31] That's called installing it on bare metal.
[10:34] But in general, it makes way more sense to run these software applications and services within containers.
[10:42] Using a container is like putting your software apps into these neat little boxes so that they don't interfere with each other.
[10:50] I prefer using the Docker container runtime.
[10:53] Now, with Docker installed on all of your home servers, you're able to cluster your servers together to form a more powerful compute cluster using this tool called Docker Swarm.
[11:09] This is Docker's built-in container orchestration tool.
[11:13] Now, once you get Docker set up, you'll want to install a number of applications that are used to visualize and manage the state of your physical servers, your Docker containers, and the software applications that are installed within those Docker containers.
[11:31] For monitoring and visualization of the physical servers, I prefer using Prometheus to do the monitoring and Grafana to do the visualization.
[11:41] And for managing containers, I prefer this nifty little tool called Portainer.
[11:47] Portainer allows me to see all the containers, to manage those containers, and to be able to read things like logs for each container and get shell access directly into these containers.
[12:00] And the funny thing is, Portainer itself runs within a container.
[12:06] Finally, I have a dashboard web application called Heimdall.
[12:10] It's basically a web page filled with links to my self-hosted services.
[12:15] And speaking of services, in general, I prefer to use open source software for all of my home lab services.
[12:24] And that's because open source software is free.
[12:28] And once you download the software, you own it.
[12:31] And if you want to modify it and customize it to suit your own needs, you can do so.
[12:37] All right.
[12:38] Let's dive into some really useful home lab services that I use.
[12:43] So Home Assistant is a home automation platform that's designed to run locally within your home lab.
[12:51] This platform allows you to integrate with all sorts of sensors in your home network that pulls in physical environment information like light, temperature, pressure, humidity, motion, human presence, and so on.
[13:09] With this environmental information, Home Assistant can then visualize and automate your internet connected devices that do something.
[13:19] Right?
[13:20] Like smart lights, smart plugs, smart speakers, thermostats, and even autonomous household robots.
[13:30] This free software basically replaces big tech's home automation solutions like Apple HomeKit and Amazon Smart Home.
[13:40] What I find really amazing about Home Assistant is that this software platform integrates with almost all internet connected home automation devices out there.
[13:52] So you're not locked into a specific vendor ecosystem like Google's or Amazon's or Apple's ecosystem.
[14:00] Now, home automation is an incredibly cool concept that probably deserves its own V-log.
[14:07] But in terms of saving money, Home Assistant saves me money in two ways.
[14:13] The first way is through its environmental monitoring and automation capabilities.
[14:19] It saves me money on energy costs.
[14:21] Home Assistant can automatically turn off lights and appliances when no one is around.
[14:28] The heating and air conditioning around the house can be automatically adjusted based on environmental information.
[14:37] Like time of day, ambient external temperature, or human presence.
[14:42] All told, these automated adjustments saves me about $50 a month in reduced energy consumption.
[14:50] The second way it saves me money is by providing free remote vehicle telematics data.
[14:57] I did this by plugging a small $10 OBD2 dongle into my used cars.
[15:05] I installed this Torque app on my Android smartphone.
[15:09] With this in place, I'm able to collect vehicle information like GPS, speed, odometer, engine diagnostic data, while in the car.
[15:21] That data is sent from the dongle to my smartphone and then streamed from my smartphone into Home Assistant in near real time.
[15:30] This kind of vehicle data is incredibly helpful for vehicle tracking and preventative maintenance.
[15:38] Now, Honda offers a similar paid subscription service for $10 a month.
[15:44] So that's how much it's saving me.
[15:46] Another super useful Home Lab service is Frigate.
[15:50] Frigate is a network video recorder, or NVR.
[15:54] It captures real-time video feeds from various IP cameras that are around my house.
[16:01] It takes that video data, stores it within my home lab, and analyzes that video footage with an AI vision model.
[16:09] This then allows Frigate to detect unusual behaviors involving people, animals, vehicles in places where they should be.
[16:21] Frigate is able to do this detection locally and in near real time.
[16:26] Once it finds an unusual event, it can save a clip video of this event and then send me an alert via my smartphone.
[16:35] A similar NVR security system, like the Ring Camera system for example, costs around $15 a month for the same functionality.
[16:45] One ultra useful Home Lab service is Nextcloud.
[16:49] I use Nextcloud for storing, managing, searching, and retrieving all of my digital documents and files.
[16:57] Think of Nextcloud as a local replacement for Box or Google Drive.
[17:03] It works in the same way and can be accessed via the web browser or through a smartphone app.
[17:09] Nextcloud saves me about $10 a month.
[17:12] Now, secure management of our passwords is very important.
[17:17] Many people use online cloud-based services like 1Password for managing their passwords.
[17:24] For this, I use a Home Lab service called Vault Warden.
[17:30] This service is free, open source, and has strong end-to-end encryption to protect your passwords.
[17:36] The other convenient thing about Vault Warden is that it allows you to get your passwords through all the usual channels.
[17:43] Like there's a web application that you can go to, there's a Chrome browser extension to get your passwords, and there's a mobile app.
[17:51] This service saves me about $5 a month.
[17:54] Now, a virtual private network or VPN gives you secure remote service to your own home network.
[18:03] A VPN encrypts your data, right?
[18:05] So, let's suppose you're in a public, unsecured Wi-Fi in a cafe somewhere.
[18:10] The VPN can prevent hackers from intercepting your sensitive data.
[18:15] Generally, VPNs cost money.
[18:17] But I have a Home Lab service called TailScale that secures remote access to my home network for free.
[18:25] It saves me about $5 a month.
[18:28] Now, a great use case for Home Labbing is to store and manage your media files, right?
[18:35] Media like photos, videos, music, and so on.
[18:40] Normally, this is managed via paid subscription services like Netflix, Hulu, iCloud Plus, and Spotify, where you can consume this media, but you don't actually own it.
[18:54] Instead of using these paid subscriptions, I use a Home Lab service called Jellyfin to store and manage all of my media files.
[19:03] The nice thing about Jellyfin is that it's accessible from a web browser, from a mobile app, and practically all smart TVs.
[19:11] Now, apart from hosting your own media, you can also automate the discovery and downloading of additional media content with a couple of other apps.
[19:24] Qubit Torrent for the actual downloading of media files.
[19:28] Sonar for discovering movies.
[19:31] Radar for discovering TV shows.
[19:34] And Lidar for discovering music.
[19:36] Now, I want to mention one very important thing.
[19:40] You do not want to pirate media content.
[19:44] You should only download media content that's either free or you have legal rights to it.
[19:51] Remember, with great power comes great responsibility.
[19:55] Anyways, getting rid of all of these media subscription services would save about $35 a month.
[20:02] Now, for the software engineers and techies out there, suppose you're building a complex software application and you need to set up a lower environment to test this application out in.
[20:14] There are all of these components that need to be provisioned and orchestrated for such an environment.
[20:21] Components like databases, app servers, automation workflows, event streams, web proxies, load balancers, and so on.
[20:32] If we were to purchase these web services from public cloud services like AWS or Microsoft Azure, that would amount to a hefty sum of money every month.
[20:43] But with a home lab, you can provision local containerized versions of these same web services.
[20:51] And you can orchestrate these containers using tools like Docker Compose or Docker Swarm templates.
[20:58] So instead of using Amazon web services, you can use local web services.
[21:05] This saves me about $50 a month.
[21:08] Finally, you can run AI large language models directly on your home lab.
[21:14] I use a service called Olama to do so.
[21:17] Now, don't get me wrong.
[21:18] Most home lab setups do not have the hardware resources to actually run a modern frontier large language model.
[21:28] Think ChatGPT 5 or Claude Opus.
[21:31] These models have trillions of parameters and require an insane amount of memory to actually run.
[21:37] Instead, I run much smaller optimized language models that are designed for edge computing devices.
[21:47] These models top out at 1 to 2 billion parameters.
[21:51] My current favorites are Google's Gemma model and Liquid AI's LFM2 model.
[21:57] Now, these models, while being very small and resource efficient, they're also quite useful.
[22:04] I use these models all the time for searching for information and for creating text and copy.
[22:12] They can be strapped into an agentic harness to do basic programming and scripting as well.
[22:18] Running entirely locally within a home lab, these AI models will work even when there's no internet connection.
[22:27] It's sort of like having a genie with a distilled version of all human knowledge living inside of your computer.
[22:36] So, with that said, Olama saves me about $20 a month in terms of purchasing less tokens from Anthropic and OpenAI.
[22:46] So, all together, my little home lab saves me about $200 a month.
[22:52] And that's pretty awesome.
[22:54] I love saving money.
[22:56] But this home labbing thing is about way more than just saving money.
[23:00] In my humble opinion, huge corporations are trying to steer our society towards a kind of techno-feudalism.
[23:09] Where the average person is entirely dependent on these digital services to just survive every day.
[23:16] But that person will not own any of it.
[23:19] Not the hardware.
[23:21] Not the software.
[23:22] Not even their own data.
[23:24] Essentially, they want people to become digital serfs. Having a home lab allows you to become much more independent of these digital services. It allows you to seize the means of compute, own your own data, and in doing so, it allows you to regain your digital sovereignty.
[23:46] And that's all I have to say about that. Hope you found it helpful. If you have a morbid curiosity to join me in this life journey, please feel free to subscribe to my channel and subscribe to my Substack newsletter. If you want to support my V-Log creation efforts, please feel free to become a member of this channel or just buy me a coffee. If you want a one-on-one coaching session, just schedule a meeting with me. Anyways, thanks so much for watching. Talk soon.
[24:16] Bye.