---
channel: "Asian Dad Energy"
video_id: "sej4OP1r-l0"
title: 'At 5AM I Passed Out at Work… Then Everything Changed'
published_at: "2026-03-20"
duration: "14:35"
word_count: 12197
---

# At 5AM I Passed Out at Work… Then Everything Changed

[00:00] Hello world, I'm an unemployed ex-big tech software engineer with 25 years of experience in tech.
[00:06] So, in my involuntary early retirement, I'm often cooking for my family.
[00:12] Today I'll be making some stir-fried pork and turnips.
[00:15] While doing so, let me regale you with an old tech war story from days gone by.
[00:21] It was early 2010.
[00:25] The tech world was crawling out of the great financial crisis like a hungover college student promising to never drink again.
[00:33] Meanwhile, I was working at a digital consulting agency and had just survived the project from hell.
[00:40] Naturally, the reward for surviving that ordeal was... another project.
[00:45] The client for this new project was a big luxury car manufacturer.
[00:50] Let's call them Clio.
[00:52] Now, Clio was one of a handful of big client accounts that our company still had.
[00:58] Clio wanted a shiny new brand website powered by a content management system, or CMS.
[01:06] The pitch was simple.
[01:08] Non-technical staff can create and publish content without developers.
[01:13] Amazing.
[01:15] Turns out, nobody in their in-house IT team knew how to build a CMS-based website.
[01:21] And that was the angle that our executives used to sell this project in.
[01:26] We would help Clio build their CMS website, along with their IT staff.
[01:31] And we would do so on an insanely aggressive schedule.
[01:35] Now, this wasn't just a website.
[01:38] This was an experience.
[01:40] Thousands of pages explaining why spending six figures on a two-ton metal rectangle would transform you into a powerful, elegant, borderline mythical being.
[01:53] You weren't buying a car.
[01:55] You were buying a personality upgrade.
[01:57] At the center of it all was the vehicle configurator, where potential customers would configure online the vehicle that they were interested in buying.
[02:07] They would configure things such as the paint, trim, interior furnishings, accessories, and so on.
[02:14] Now, all of this detailed vehicle configuration data would be combined with inventory availability data and then sent downstream to a customer-selected dealership as a kind of request for a quote on this customized vehicle.
[02:29] Then, the customer can visit the dealership in person, and the dealer would have not only the quote for the vehicle, but also the logistical inventory information on whether that vehicle is available or not.
[02:42] So, I rode onto this project as the backend tech lead and got a good look at the team.
[02:48] Along with me were Tyrone, senior backend developer, Brian, a junior backend developer, Sudarshan, Clio IT backend developer, Andre, the frontend developer lead, Sarah, a junior frontend developer, Jaten, Clio's IT frontend developer, and our super friendly project manager, Jake.
[03:13] Now, I reported up to Nigel, an enterprise architect with a thick working-class English accent.
[03:20] Nigel, in turn, reported to Alan, our technical director, and Alan, in turn, laddered up to Haley, client executive VP for this account.
[03:30] Now, I soon learned a bit about the architecture of this project, and just how much our hands were tied.
[03:37] The client had somehow already purchased an enterprise-grade CMS for huge amounts of money.
[03:43] Let's call this CMS Portrait.
[03:46] They did this before they had even determined the full requirements of their project.
[03:51] Well, it turns out that Portrait could only render web pages that looked straight out of the 1990s.
[03:58] As such, we basically had a situation where the non-technical users are going to be entering content into Portal's admin page.
[04:07] Really, just a gray web page with a giant list of forms and fields.
[04:11] And that entered content has to be then published as these gigantic XML feeds into a bespoke Spring MVC web application that we were building.
[04:22] Once there, that XML content would be parsed and reformatted by the web application into sleek and modern-looking web pages.
[04:30] In retrospect, this architecture almost defeats the purpose of having a CMS, since the content author cannot easily preview the impact of their content changes on the pages that they were working on.
[04:44] Now, in terms of the vehicle configurator, I soon learned that Clio's dealership networks were almost like a collection of fiefdoms decoupled from their corporate overlords.
[04:56] And at that time, Clio's corporate IT did not have a consolidated enterprise middleware layer.
[05:03] So each group of dealerships had their own bespoke mechanism for communicating vehicle quote requests and inventory information.
[05:12] These mechanisms were a mix of relatively modern SOAP-based APIs, POX, or plain old XML interfaces, and a few archaic Korba integrations from the late 90s.
[05:25] And our new website had to integrate with every single one of them.
[05:30] Now, the squad got off to the races rather quickly.
[05:33] The project seems to have transitioned from relaxed to focus mode in a matter of a few weeks.
[05:39] Pretty soon, we were working super long hours every day, and in doing so, I got to know the team pretty well.
[05:47] For one thing, I liked Nigel.
[05:50] He was a very hands-on architect, often coding some of the hardest components that he himself had designed.
[05:57] He was quick to help me out, and very blunt with corrective feedback.
[06:01] And that ultra-working-class English accent of his, All right, lads, it's rubbish.
[06:07] Good enough for government work.
[06:10] Made the entire operation feel like we're in some kind of a 19th century garment factory.
[06:16] Now, Andre was an exceptionally capable front-end developer with great leadership potential, and he had this habit of telling ultra-sarcastic but equally funny jokes.
[06:29] Darshan, an H-1B developer who had somehow survived multiple rounds of mass layoffs at Clio.
[06:35] He had a three-month-old baby at home and this weird thousand-yard stare of quiet desperation.
[06:42] Brian and Sarah were your typical junior engineers.
[06:46] Young, idealistic, and filled with imposter syndrome.
[06:50] Haley was non-technical, but she had this intuitive understanding of people and seemed to command their respect and attention.
[06:59] Haley could somehow see gaps and fissures within the various client teams and seamlessly maneuver conversations with Clio's executive leadership.
[07:10] And in doing so, she always ensured that our consulting agency had a solid foothold within their corporate hierarchy.
[07:17] Seeing her talk to client leadership was like witnessing some kind of poetic black magic.
[07:25] Now, as for Alan, Alan was quite possibly the strongest engineer that I've ever met.
[07:31] He knew both front-end and back-end development across several different tech stacks, and he knew this stuff like the back of his hand.
[07:38] Alan was a very big, muscular man who showed up to work in beach shorts.
[07:44] He worked like a dog and drank wine throughout the day.
[07:48] Alan was very straightforward, and sometimes it was shocking and other times hilarious.
[07:53] I still remember one evening, Alan was educating us on the intricacies of juggling two girlfriends at the same time while drinking and debugging a Korba object hydration issue.
[08:06] Now, I deeply respected both Alan and Haley, but for some reason, they didn't get along with each other all too well.
[08:13] So, we kept grinding out this project.
[08:18] Progress was being made, but the deadline for code completion was rushing towards us like a freight train.
[08:24] Now, back then, we were using the waterfall development methodology.
[08:29] And with waterfall, every major stage of a software project had hard delivery dates attached, and we had to make these dates come hell or high water.
[08:39] As the code completion deadline approached, the working hours got progressively longer and longer, until we were pulling 12-hour workdays every weekday and working some weekends.
[08:51] Then, about two weeks before that deadline, the team started to visibly crack under the pressure.
[08:58] You see, at this point in 2010, the tech jobs market was beginning to recover from the Great Recession, and developers were starting to find work again.
[09:09] But our company still expected a death march level of commitment from the team, as if we were still in 2009.
[09:17] So, in a span of just two weeks, our team got decimated.
[09:21] First, it was Tyrone, who found a much higher-paying gig.
[09:25] He was followed by Jaten, who quit Clio for greener pastures.
[09:30] Jaten was then followed by Nigel, our architect, who left for a better position.
[09:35] Then Jake, the project manager, left the project, just three days before the delivery deadline.
[09:42] Then, on the last day, Sarah showed up to work visibly upset.
[09:45] After some small talk, she opened up to us on what happened.
[09:49] It turns out that she was being paid significantly less money than other junior developers, ever since she got hired.
[09:57] And after a while, she said she's not in the mental state to work today and took the rest of the day off.
[10:03] So, at that point, the team was down to just Alan, Andre, Brian, Sudarshan, and me.
[10:10] Our application had to be code complete by the next day, but being so shorthanded, we realistically needed another week for this work to be done.
[10:19] So, we coded like madmen throughout that final day.
[10:23] It felt to me like any kind of code quality was falling by the wayside, and we just had to get all of these components finished before the review with our client executives tomorrow.
[10:34] That evening, Alan ordered us a huge tray of wings, and he brought several huge bottles of wine.
[10:42] We ate the wings, drank, and coded like maniacs.
[10:46] At around 1 a.m., Sudarshan got a call from his wife.
[10:50] After the call, he looked visibly upset.
[10:53] Sudarshan apologized and told us that his baby was feverish and that he had to go home.
[10:59] At that point, Brian, the junior engineer, got angry.
[11:03] How can you leave us hanging like this, man?
[11:06] It ain't fair.
[11:07] Brian, he got so worked up that his face turned beet red.
[11:12] It looked to me like Brian was about to have a fist fight with Sudarshan.
[11:17] So, I quickly put myself between these two guys, and I asked Brian to chill the heck out, and I told Sudarshan that he can go home to his wife and baby.
[11:26] So, we just kept on coding and coding, and at some point during that night, Brian, I don't remember if he left or just crashed out, but he just disappeared.
[11:37] And by then, we still had many components left to code out.
[11:41] At some point, around 5 a.m. in the morning, I hit my breaking point.
[11:46] My head ached like hell, and my eyes just couldn't focus on the lines of code in my Eclipse editor anymore.
[11:54] Alan and Andre were still debugging something on the vehicle configurator, kind of like superhumans.
[12:02] At that point, I excused myself out of the war room and wandered into a small meeting room nearby called the studio.
[12:09] Once there, I crashed onto this futon couch and promptly lost consciousness.
[12:15] I woke up to this incredibly strong, musky smell in my nostrils, and the sound of a woman repeatedly calling my name.
[12:26] I opened my eyes and found that in my slumber, I had drooled all over the futon couch, and Haley, the account executive, was standing there staring at me with a curious look on her face.
[12:38] That made me a little uncomfortable.
[12:40] What's wrong? I asked her.
[12:42] She looks at me and said, Oh, nothing. Just so you know, you were sleeping on the summer intern's make-out couch.
[12:51] I jumped off that couch and rushed to the bathroom.
[12:53] I felt like we were doomed.
[12:56] The code completion deadline had passed, and we weren't nearly finished yet.
[13:00] I had failed the team, and we're going to lose this client.
[13:03] So Haley, after reviewing the state of the application, proceeded to demo it to the client executive leadership.
[13:11] She walked into that client demo like a magician entering a final boss fight.
[13:17] And somehow, she convinced the executives that, one, everything important was done.
[13:23] Two, the missing pieces, they were just minor defects.
[13:28] And three, we were in fact crushing this project.
[13:31] The clients, they loved it.
[13:34] They praised us.
[13:35] That day, I learned two important things.
[13:39] One, never underestimate the power of storytelling.
[13:43] And two, never, ever sleep on the intern make-out couch.
[13:48] Some mistakes stay with you.
[13:50] Some probably stay on the couch.
[13:53] The end.
[13:57] Anyways, I hope you enjoyed this little story from yesteryear.
[14:01] If you have a morbid curiosity to join me on this little life journey, please feel free to subscribe to my channel and subscribe to my Substack newsletter.
[14:10] If you want to support my V-log creation efforts, please feel free to become a member of this channel or just buy me a coffee.
[14:17] If you want to chat with me or have a one-on-one coaching session, just schedule a meeting.
[14:23] Anyways, thanks so much for watching.
[14:25] Talk soon.
[14:25] Bye.