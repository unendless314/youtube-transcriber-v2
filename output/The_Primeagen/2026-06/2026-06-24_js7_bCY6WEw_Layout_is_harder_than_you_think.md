---
channel: "The Primeagen"
video_id: "js7_bCY6WEw"
title: 'Layout is harder than you think..'
published_at: "2026-06-24"
duration: "21:11"
word_count: 23939
---

# Layout is harder than you think..

[00:00] All right, so we're a couple of weeks now into building with Odin and I have built a layout system.
[00:05] I'm trying this little experimental one right here, seeing how I feel a bunch of just, about a bunch of just like functions where you can start and stop elements and all that.
[00:13] And we're gonna go over this and the outcome of me building this is something that looks like this.
[00:18] Look at those nicely aligned boxes.
[00:20] I can also go out here and produce out a card.
[00:22] Look at that nice looking card.
[00:24] I can even go in here and produce out a deck that animates.
[00:28] Look at that.
[00:29] Would you look at that?
[00:30] That looks pretty dang good.
[00:32] So today I thought I would just talk about how I'm doing the layout system because it's, well, it's pretty fun.
[00:37] And honestly, I am just absurdly excited about this kind of code because I think it's gonna make things a lot easier or more fun to work with.
[00:46] All right, so let's talk about layout systems.
[00:48] The thing is, is most people, when you hear the term layout system, you probably think of something like the DOM.
[00:54] Now the DOM, any element you see on the page is a real element that you can reference, right?
[00:59] It is a DOM node.
[01:01] I can go in there and I can say, hey, create div and I can attach it to my body and then it's gonna be on there.
[01:06] That DOM node, I can do something like on click, right?
[01:09] And I can do, I can listen to all sorts of different on events and then react to that specific element, say being hovered, being entered, being exited.
[01:18] I think they call it blur on focused and blurred in the web world.
[01:24] But nonetheless, that is the DOM UI.
[01:27] And this is called retained mode because the entire tree, everything that exists, the entire UI is not generated when you need to make a change.
[01:36] Instead, you actually have pieces of memory and elements that you actually alter, which then update the UI.
[01:43] Whereas a different type of UI, the UI that I built is called immediate mode.
[01:48] Now, the very first time I built this game, Mordoria, I actually built it with retained mode UI.
[01:53] There was a bunch of things that made it super, super duper hard and I ended up solving a lot of problems with event buses.
[01:59] But this one, I think I'll be able to get out of it without any of that stuff.
[02:03] And so this is called an immediate mode UI and how this works is effectively, or at least how I'm gonna use it, which is not necessarily the only way to use it, is every single frame, I'm going to produce the entire game's UI.
[02:15] Now, there's only gonna be so much UI going on at any one point.
[02:18] Maybe I'll have like a tower being highlighted.
[02:21] Maybe there will be a bad guy that's being highlighted showing how much health or whatever he has.
[02:25] Maybe I'll have some gold that's being incremented or I'm looking at the stats of an individual tower.
[02:30] But nonetheless, or there could also be a whole bunch of cards on the map, right, at the same time.
[02:35] But nonetheless, there's only so many elements here, something like, I don't know, 50 to 100 at max.
[02:41] And so regenerating those is gonna take virtually no effort to be able to do.
[02:46] The real cool or hard part about a layout system is actually doing all the math.
[02:51] Now, I watched a video called How Clay's Layout Algorithm Works.
[02:55] I actually watched that video and attempted to copy a good portion of its features.
[03:00] Now, I'll give you the TLDR, but you should go watch it if you're actually interested in how immediate mode, like world-class immediate mode kind of layout systems work.
[03:10] Now, so for me, what I did is I only needed a few things.
[03:13] I wanted to be able to create a box and then horizontally align a series of elements inside of that box.
[03:20] Next, I wanted to be able to do the same thing, but maybe vertically align a series of those elements within the box.
[03:26] That makes sense.
[03:26] I also wanted to be able to create a box and then be able to center a div inside of that box.
[03:31] I know, centering.
[03:32] The world's most impossible problem.
[03:35] So I just wanted to be able to do like a few things.
[03:38] And so the rules that I came up with is that every leaf node has effectively three different ways it could have a size.
[03:45] First, it could be a fixed size item.
[03:46] Hey, this thing's a 50 by 50 square that exists.
[03:49] Two, it could have text.
[03:51] There are just text on the screen and that's how big the item is.
[03:56] Or three, it has a sprite and the sprite has a defined size.
[04:00] That's how big the item is, the end.
[04:03] And so from these three different types, I can build the rest of the system actually pretty dang easy.
[04:09] So to give you kind of like the quick idea of how a layout system can work is that first I take a box, right?
[04:14] And then inside of it, I create three items.
[04:16] Now, I don't know where those three items should be placed, right?
[04:19] I don't know anything about them.
[04:20] I just know they have a fixed size.
[04:22] And what I ideally would like at the end of the day is those three boxes centered.
[04:26] Now, some are obviously gonna be closer to the edge.
[04:29] Some will be less close to the edge and others will be, you know, the most far, right?
[04:34] That's kind of what I would expect to have happen.
[04:36] And so what you have to do when you do a layout system is you have to walk down this UI tree and you need to walk down it in a post order traversal.
[04:45] That means you get all the way down to the leaves, calculate the size of just the children.
[04:50] Now, since the children all have a defined size, that's easy.
[04:52] But then any of the auto laid out boxes, which by the way, this box should be like this big, right?
[04:57] It should not be that big right there.
[04:58] That box, it depends on how big your kids are.
[05:03] And since you already know the size of your kids, all you need to do is know the size of the padding on each side.
[05:08] You need to know the size of the gap in between the kids and that is your width.
[05:13] It's actually not that hard.
[05:14] And the height is also interesting because it's just the padding and then it's the height of the biggest child element.
[05:21] And this is the exact same thing as you would do vertically.
[05:24] The only difference of course is that you would use the width, the biggest width as how wide your box should be.
[05:29] And then the height should be the sum of your kid's height plus the gap, plus the padding.
[05:34] And this is it.
[05:35] This is largely part of the algorithm you have to calculate to be able to do this kind of work.
[05:40] There's a lot of other stuff, but this would be the sizing side of things, which actually was not all that bad.
[05:47] Now, here's the deal though.
[05:48] After you figure out the sizes, you are then able to figure out the positions.
[05:52] And that makes total sense, right?
[05:53] Because if you have three elements inside of a box and you know there are three sizes, that means you put the first one in and then you go, okay, well, based on the padding right here that you can see, plus the width of the first kid, plus the gap, that's where the next one starts.
[06:08] And then that is gonna be, okay, the width plus the gap, that's where the next one is going to start.
[06:13] And you're able to easily lay things out.
[06:15] And then if you do any sort of alignment while you're doing positioning, you can say, okay, I'm trying to center it in the off axis.
[06:22] By the way, there's the off axis, which is the opposite direction as the alignment direction.
[06:26] The off axis, all I have to do is say, okay, take your parents' height minus your kid's height, right?
[06:32] The element's height.
[06:33] And then divide that by two.
[06:35] Then boom, you got this height right here.
[06:37] Okay.
[06:38] So you already know how to center them.
[06:40] It's not even that hard.
[06:41] Which is this code right here, which is actually just a touch longer.
[06:44] Okay.
[06:44] It's a little bit longer.
[06:45] Okay.
[06:46] Because there's also alignment.
[06:48] Look at it.
[06:49] Would you look at all that code?
[06:50] But hey, I wrote all that code.
[06:51] It feels good.
[06:52] I know what's going on here.
[06:54] Like I know what's happening right here.
[06:55] And this makes me happy.
[06:56] And so this was actually my first time ever building an immediate mode UI.
[07:01] And I can see why there's some advantages.
[07:03] Now you're probably thinking, well, what are the advantages?
[07:05] What are the trade-offs?
[07:06] Well, one of the big trade-offs is actually how mouse works.
[07:09] Now let me give you an obvious and simple example of why this could be complicated.
[07:14] So as I explained, to be able to do a layout like this, you first have to calculate the size of every item.
[07:20] Then you can calculate where they are at in the universe.
[07:23] Now what happens if I have a mouse right here and when that happens, I want this element to scale.
[07:29] How would I know the mouse is inside of that box if I haven't already laid out the size and then the positioning?
[07:38] You can kind of see there's a bit of a chicken and an egg problem.
[07:41] I have a mouse at this position of the screen.
[07:43] Well, how do I know this thing needs to be expanded?
[07:45] Well, I only know it needs to be expanded because I already know where it's at.
[07:48] Well, I only know where it's at by rendering everything out.
[07:50] Well, if I render everything out, then I don't know that the mouse is there.
[07:53] So I don't say, hey, become big.
[07:55] So it's almost like, do you have to lay it out twice?
[07:58] Is that the answer?
[07:59] No, you ignorant slut.
[08:01] That's, of course, that's not the answer.
[08:02] You're completely wrong.
[08:03] So this is how I solve it.
[08:05] So I take the root and I save my root of my layout.
[08:09] And so at the very beginning first frame, I go and get the mouse info.
[08:13] Of course, the mouse info is just going to Raylib saying, hey, give me your XY and if the first button is down.
[08:17] After that, I go in here and calculate the mouse based off the previous route.
[08:22] Obviously, if there is no route, we just leave.
[08:25] Else I do this beautiful descend algorithm, which is actually pretty simple.
[08:29] And I just get to the very bottom of the tree and say, hey, if the mouse is inside of my rendered rectangle, then I can do things like, hey, are you held?
[08:38] Are you entered?
[08:38] Are you exited?
[08:39] Are you hovered?
[08:41] Have you been dragging?
[08:42] Like I can just do all the calculations in one simple little spot.
[08:47] And it just works.
[08:49] It's simple.
[08:51] It's nice.
[08:51] It makes me feel happy, honestly.
[08:53] And it's not even that much code like the entire mouse library, including this gigantic, what's it called?
[09:00] The bugging statement and this gigantic resetting statement and this mouse and rectangle statement, which are all pretty large, actually only ends up being less than 200 lines of code.
[09:09] And it's really easy for me to understand.
[09:11] So that means the first time I try to do anything with the mouse for the first frame, I can't do anything.
[09:17] Totally okay.
[09:18] But the next frame, I know where everything was.
[09:21] I test my mouse against it.
[09:22] And then when everything renders and goes, okay, was the mouse in me?
[09:26] It was.
[09:26] I need to start expanding.
[09:28] And so that way I get this nice, beautiful effect where everything knows where the mouse is and what state it is in inside of rendering.
[09:35] And this is kind of like the big bonus of immediate mode.
[09:37] See, with retained mode, you have to have all these like function handlers that like when the mouse enters, you have to keep state, right?
[09:43] You have to be like, okay, I am, I'm actually hovered right now.
[09:46] Okay, I'm hovered.
[09:47] And I have to wait till some other function somewhere else executes and says, okay, I'm no longer hovered anymore.
[09:51] So you have to do all this kind of like state management that's really, really confusing.
[09:56] But instead with immediate mode, I construct the UI and during construction, I can go, am I hovered?
[10:03] Oh, I am hovered during this moment.
[10:05] Then I should be 2x the size.
[10:07] And mixing in animations honestly is not all that hard.
[10:10] It's pretty straightforward because once you have the whole idea of, hey, what is my state at this current moment?
[10:15] And I only build my UI based off that state.
[10:18] It actually makes everything else pretty dang simple.
[10:22] I am super shocked at how much I like immediate mode UIs.
[10:27] But of course, at that point, I wasn't happy.
[10:29] So I created this little helper item because when you're building stuff, right?
[10:32] So if I go to my components card and I go and look at what it takes to build, if you go all the way down here, that's like a previous one that I vibe coded up just to see what it would take.
[10:41] Like here is my card being built and I build up the params, all this kind of stuff.
[10:45] That means every element I build has to have these like large kind of parameter objects and they're kind of just ugly and I don't really like reading code like this.
[10:52] It just feels annoying.
[10:54] And if I want to do any sort of calculations, it's kind of like, you know, annoying to do those calculations when you have these big structs and all that.
[11:01] And so every single, like every single element construction just looks like this, which I find very unappealing as a programmer.
[11:08] Now, obviously as an AI, this is very, very easy.
[11:10] If I just showed my AI and built up a nice couple examples, I guarantee you I could generate the crap out of this.
[11:17] Not even a problem at all, right?
[11:19] Well, buddy, I'm not an AI and I actually have this belief.
[11:22] It's kind of a silly belief that code should feel aesthetic.
[11:26] I should really like the experience.
[11:28] So I came up with this silly, silly, really, really silly idea.
[11:32] And I don't know if it's actually going to be any good, but here's the idea.
[11:35] At the very top of my Odin file, I have this kind of like module level variable.
[11:40] Honestly, I could probably, I should probably just call it private.
[11:42] I don't want anyone touching that.
[11:43] Okay.
[11:43] That would be gross.
[11:44] Please don't hate.
[11:45] Please don't touch my privates.
[11:46] Okay.
[11:46] Very inappropriate.
[11:47] Anyways, what I do is I have a start function.
[11:50] This starts a UI building process.
[11:52] And what it does is it's going to allocate on the temporary allocator a bunch of layout handles.
[11:58] All right.
[11:58] It's okay.
[11:59] I'm sure I could do this better.
[12:00] Honestly, I think I could do this better.
[12:02] But for now, let's just stick with this because I just wanted to, you know, whip out something.
[12:06] And my current index equals negative one.
[12:08] Then I call start element.
[12:10] When start element happens, I get the index into elements.
[12:13] I create a new layout handle with the temporary allocator.
[12:16] Very good, by the way, for those that don't know what a temporary allocator are, it's like one of the coolest things ever.
[12:20] So in managed memory languages, what ends up happening is that you have to go and you have to go and call malloc on a bunch of items.
[12:27] And these items get allocated somewhere off in the heap that you don't know where they're at.
[12:31] And then you have to remember, okay, hey, my structure, I need to deallocate this.
[12:35] Because if you don't, malloc will think, okay, this thing exists forever.
[12:38] I will know, I can't ever use that memory.
[12:41] It's forever there.
[12:41] Forever, forever, forever.
[12:42] And they call this obviously leaking memory.
[12:44] It's very easy to do this in a managed language, but it's even easier to do this in you're the manager language.
[12:50] And Odin's a, you're the manager language.
[12:51] But it has this idea of a temporary allocator.
[12:54] So does Jai, by the way.
[12:54] Beautiful concept.
[12:56] Absolutely love it.
[12:57] Which is, at any point, I can call free on the temporary allocator.
[13:01] And everything that was allocated by it goes away.
[13:04] So as you can see here, here's my main game loop.
[13:07] I can just go free at the end of every loop.
[13:11] And everything that I allocated during that loop, it's gone.
[13:15] I didn't have to keep track of it.
[13:17] I didn't have to worry about it.
[13:19] It's just this nice, really simple allocator.
[13:22] Because if you think about it, that means the internals to that allocator can be dirt simple.
[13:26] Just allocate to the left.
[13:29] Right?
[13:29] I don't have to even think about it.
[13:31] Or actually, technically, I guess I look at it as allocate to the right.
[13:33] Allocate to the right.
[13:34] I even pointed to the right.
[13:36] But just keep on allocating to the right.
[13:39] And then when they say done, you go, okay, done.
[13:42] Back to zero.
[13:43] Keep on allocating.
[13:44] It's actually a really, really, really beautiful concept.
[13:47] Absolutely love it.
[13:48] Anyway, sorry for the side quest there for a second.
[13:50] But then I create these elements, these element handles, right?
[13:53] And it has, okay, I have no parent.
[13:54] Here's my index.
[13:56] Here's my parameter.
[13:57] See that big, ugly parameter object.
[13:59] I don't have any children.
[14:00] I'm going to say I'm on just on axis X.
[14:02] That's what it is.
[14:03] And I'm going to append this to my dynamic elements array.
[14:06] Again, I think I could just hard code this and I don't have to do all this.
[14:08] But for now, whatever.
[14:09] If my index is greater than zero and my current index is greater than zero, that means I am already in the tree starting elements.
[14:18] So I'm actually a child somewhere.
[14:20] And so that means I can actually get the parent thing and say, okay, hey, one of your children is me and my parent is you.
[14:28] And now I've kind of created this nice tree situation in the order in which you call start element.
[14:33] End element just does the inverse, right?
[14:35] It goes, okay, grab my current element.
[14:38] If the index is zero, we're done.
[14:40] We're out of the tree.
[14:41] Else, the current index is the parent index.
[14:44] Okay, we're going to jump back one.
[14:45] I'm using the term index because again, I was thinking about doing like a hard coded array and just handing out references into this one single contiguous piece of memory.
[14:53] I might just go to that.
[14:55] So I'm kind of keeping the index idea around.
[14:56] I don't really know what I'm doing.
[14:58] Okay, I'm a noob.
[14:59] So therefore, from there, I can actually go again, temporary allocator.
[15:02] I can create a dynamic array, get all the children elements from it and go and call my layout system with the next set and create a new element.
[15:12] So I'm actually creating elements up the tree as those functions are being called.
[15:16] Then lastly, I just create a series of really nice functions that can work with the current element.
[15:20] Like, hey, I want to be able to create a background color.
[15:23] Okay, grab the current element, set its parameters to the background color.
[15:26] You must at least have an element.
[15:28] I should never make this mistake in code.
[15:29] There should always be an open element going on right there.
[15:31] By the way, asserts on conditions that cannot be broken.
[15:34] Absolutely love it.
[15:37] By the way, one of the best things you can do.
[15:39] So with that, I was able to create this nice little UI right here, which is, okay, I'm going to start a row.
[15:44] Okay, it's horizontal.
[15:45] I want this padding.
[15:46] I want this gap.
[15:47] Okay, for every element, I want to start the element, give it a size, give it a background color and the element.
[15:52] And then I'm just going to return out the results of end element, which of course is one of my layout items.
[15:57] And bada bing, bada boom, I just created a UI.
[16:02] And of course, that's the UI that I was talking about earlier.
[16:05] That little pretty thing right there.
[16:06] Anyways, I wanted to talk to you about that because I've never built a UI like this.
[16:10] I've never tried this kind of unique, I guess, kind of style of building a UI.
[16:14] I just wanted to see what it would feel like.
[16:16] See if I actually like it.
[16:17] I'm going to incorporate it into a game, write thousands of lines of code of UI code, and I'll be able to tell you at the end, was I happy with this style for how simple my game is?
[16:26] My guess is that I'm going to be pretty happy about it because this is code that I consider beautiful, right?
[16:31] Like I look at that and I go, I like the looks of that code.
[16:34] Now, do I need to be able to do this like temporary allocator new stuff?
[16:37] Probably not.
[16:38] Honestly, I think I could do something like max elements, right?
[16:42] And just be like, hey, there is a maximum amount of elements that you can have and that's just that.
[16:48] And then I can just point to each one of them is my guess.
[16:50] So instead of doing a make, I just set my index back down to negative one and then I just simply have to have something like, you know, a count, which is going to have to be zero.
[17:00] And it's going to be like, okay, well, count's zero.
[17:03] So I'm just going to get, instead of getting the length of the elements, I get the current count and then I can just point to this thing and then it's all in just one nice little array and I don't have to do any of this
[17:11] make temporary allocations.
[17:13] But I also have a sneaking suspicion that none of that is going to matter at all.
[17:17] I have 50 items and that means I'm going to draw draw like a few of them a second.
[17:23] I don't know, a few hundred, 3000, 3000 operations in a second.
[17:28] Easy peasy, pumpkin, squeezy.
[17:31] Whatever that amount of work is, it's going to be only a fraction of the power that React requires anyways and I think I'm going to like it more.
[17:38] And I wanted to talk to you guys about this because I really do think the immediate mode style UI actually is just super duper cool.
[17:46] Honestly, it is a little bit like React in the sense that React wanted to be this really declarative UI that you can just read from top to bottom.
[17:54] Now I know, I've read a lot of React, that's not actually what happens, but you get the idea.
[17:58] You should be able to be like, oh, you're building this thing and then you're building that thing and then you're building that thing.
[18:02] Oh yeah, it's very straightforward and you read it declaratively.
[18:06] I understand this is very imperative, but in a sense it also feels very declarative.
[18:11] Like, I know that I'm starting an element.
[18:13] I have these things.
[18:14] I'm building these things one at a time.
[18:15] It feels very like visually obvious what is happening here.
[18:18] And the thing that, again, I said this in the beginning that I love the most is when it comes to like handling mouse operations, I just, in one frame, make one decision.
[18:28] I don't have to have crap spread around everywhere and this state kind of schmeared everywhere saying, okay, well, me, the card,
[18:38] I was dragged, so therefore, I need to tell the deck that I was dragged, like the deck goes, okay, how far was the card?
[18:45] Dragged it.
[18:46] Oh, the card was dragged it outside of its range, therefore, it needs to leave me.
[18:50] I better go tell the event bus that I am actively about to play a card and so then the card knows that it's about to be actively played so then the card needs to sparkle.
[19:00] It's like, my gosh, that is so much weird indirection of like, how you tell different components what to do.
[19:10] Instead, I can just simply have a function now that's like, okay, hey, what's the mouse state?
[19:15] Oh, okay, dragging is happening?
[19:16] Oh, it's a card?
[19:17] Okay, the card is being dragged.
[19:19] Okay, it's actually within the playable range.
[19:22] Hey, I'm going to draw the card like this.
[19:25] The card, it's playable currently and deck, you look like this currently.
[19:28] Like, I can make decisions outside of everything in this really smooth, easy way.
[19:33] Just, it makes me feel good because you make decisions in a non-stateful way just in the snapshot of the state.
[19:41] Beautiful.
[19:44] That's it.
[19:45] That's all I wanted to talk about.
[19:46] I know this video is a bit rambly, but I'm having a lot of fun, okay?
[19:50] And it looks like you guys are also enjoying that. 1.1,000 subs?
[19:54] Hey, appreciate it.
[19:55] This was my first video into Odin.
[19:57] Now I'm doing the second one, so I hope, I don't know, I hope everyone enjoys it.
[20:02] Hey, next week though, we'll figure out something better to talk about, okay?
[20:06] Because I think I'm going to start getting into components, building a lot of components and handling mouses and all that kind of fun stuff.
[20:11] I also want to talk about snapshot testing.
[20:13] I think I'm pretty happy with how I'm doing that where I can say, okay, hey, I want to be able to test all these different kind of card states and I want to be able to test all these
[20:25] different layout states and I want to make sure they all look the same no matter what and so if I make changes to my program, I want all those images to be identical and so what that means is I can actually go like this
[20:35] without displaying them.
[20:36] I can just say, hey, go test it and it was like, okay, yep, nothing changed.
[20:41] Your previous time you rendered that, it's the same as this current time so I'm doing like some golden testing because, you know, here's one big problem I have which is you end up getting
[20:50] a game big enough or you get a program big enough, you start to kind of forget what everything you need to test to make sure everything's good.
[20:58] You kind of want just to be told what's wrong and also in the day and age of agents, the more information you can tell them, kind of the better so this makes me happy.
[21:07] Hey, the name, I will talk about snapshots again.
[21:10] Bye bye.