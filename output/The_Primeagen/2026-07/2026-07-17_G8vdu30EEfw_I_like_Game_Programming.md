---
channel: "The Primeagen"
video_id: "G8vdu30EEfw"
title: 'I like Game Programming'
published_at: "2026-07-17"
duration: "8:01"
word_count: 9316
---

# I like Game Programming

[00:00] All right, so if you've been following along, I've been building a tower defense in Odin.
[00:04] I already built like 80% of it in Lua.
[00:06] I didn't really love the Lua experience or love 2D.
[00:08] So I went with Odin, Odin being a very simple language, a C-like programming language for the love of the game.
[00:13] And so with that, I've been building out a UI system.
[00:16] I've decided to change the UI system to be this kind of like stack-based element building approach to where every time I wanna build out an element, I can just simply start this open element process, which will allow me to do a bunch of stack-based calls and then build the tree as it goes.
[00:31] And then every part of the tree can call further into every single tree and every single open method just leaves open an element such that I'm able to edit where the element's placed and how it's placed on the screen with inside, say, an if statement right here.
[00:44] I can even say how the animations will work on it and all that.
[00:47] So that way, a card that's being rendered in one spot can be rendered completely different somewhere else.
[00:51] It kind of makes this really nice, beautiful experience that I'm very, very happy about.
[00:55] But nonetheless, building your own UI and going through all that was a lot of fun for me.
[00:59] I even, by the way, just as like kind of like a little side note inside the builder, I even built my own flex elements now, which means that we're actually having our beautiful own little flex elements that say what access they're on.
[01:11] I started to go with unions and actually have subtypes of elements and made a bunch of changes.
[01:15] But nonetheless, very happy about this experience.
[01:18] Everything is super good.
[01:20] And I really liked my UI.
[01:22] I can't believe I built the UI framework I actually kind of like here.
[01:25] But nonetheless, building all that was fantastic.
[01:27] But what's the big problem about building any sort of layout system?
[01:30] Well, the moment you make any sort of change to your game, you can impact your layout system in some way in which you did not expect.
[01:37] And I didn't want to have to constantly be playing the game, making changes, and then like, I don't know, a week into developing something, realize I've screwed up some part of the layout and then try to have to like, figure out why the layout's kind of goofy.
[01:51] Like what has gone wrong with the layout?
[01:53] I don't know.
[01:54] So I built this beautiful little demo runner called Demo Test.
[01:57] So what it's gonna do is it's gonna load up all my different demos and just play them one at a time for me because I did display equal, like I added the display flag so I can just see it.
[02:04] See that button was clicked without me.
[02:06] Menus are being expanded.
[02:08] You can see opacity right here is flowing from the parent to the child and making sure it's multiplicative.
[02:12] You're also seeing like that middle element move.
[02:14] I'm doing fixed position off-axis alignment, stats tables running, boom, bada-bing, animation, everything running.
[02:20] But the best part about this is that I can remove that display and it will actually test against golden versions of that.
[02:27] And what do I mean by that?
[02:28] Well, if I go in here and say goldens, I actually get a display that brings up all the goldens.
[02:33] So this takes all my demos and it records them.
[02:35] So every time I press the mouse, it changes in between the scenes on what it saved and it makes sure that every single time I make a change to my program, I should be able to see all of these running correctly and they produce the same results every time.
[02:51] I say, hey, I want this many milliseconds to go and I want to be able to take a picture at that amount of milliseconds and see it actually happen.
[02:58] So that way I can build this game by building a bunch of demos.
[03:02] When I build a demo, I then save it and say, hey, this is how many frames I want you to save.
[03:07] Now, this is where things get a little bit clever is I built this idea called a test frame and a test frame is simply a time test frame or a mouse test frame.
[03:14] A mouse test frame is pretty straightforward.
[03:15] It's a duration plus this little mouse state right here.
[03:18] A mouse state, of course, is position.
[03:20] And if the left button is down, that means over time, I can actually take these little frames and I can play the mouse.
[03:26] So if I say, hey, take the mouse and I want you to move it to this position over 500 milliseconds, as you can see right here, it's going to lerp it and play it through my program.
[03:34] So my program actually acts as if a real mouse movement has flown through it.
[03:39] And then I can actually get the UI effects, the expands, the scales, the movements, the animations.
[03:44] And then I can say, hey, at the end of every single one of these frames, I want you to take a picture and save it.
[03:50] So instead of rendering to the screen, I render to a texture and either paint the texture to the screen if I want to see it or paint that texture to a file.
[03:58] And then I can load that file back up and test it against it every single time I run.
[04:04] So that means after every single time I run a beautiful little task, I can say, hey, agent task finalized, goes through, runs all my different unit tests, make sure I build for Windows, for Mac, for Darwin, Darwin, AMD, ARM64, blah, blah, blah, blah, blah.
[04:18] And also make sure all the demos run the exact same.
[04:23] So that means anytime I've screwed up anything, it's actually going to go and find that out.
[04:27] Because one thing I always have with unit tests or one thing I really hate about unit tests is that if you look at any of my unit tests, they're always the same crap where it's just like you have so many of these like hard-coded values, you have to go and make sure that are all actually the same.
[04:40] You have to make sure that you didn't drag like one pixel too far or else everything breaks.
[04:45] If any of these values change, things just blow up.
[04:48] And it's always so hard to kind of go through like the minutiae of every one of those details.
[04:52] But if I can mostly prove with unit tests that things are operating the way I want on the small scale, then I can do integration tests or end-to-end tests effectively where I actually have the mouse move and animations happen and I can take all the photos and everything looks beautiful.
[05:06] And honestly, I've been very happy with this approach.
[05:10] I'm actually loving it very, very much so.
[05:13] And so that's kind of the update I wanted to talk about a little bit is that that's what I've been exploring for the last week is like, how do I just not shoot myself in the foot?
[05:20] That way, if I decide to vibe out a feature, at least I know it's going to work, which by the way, I've been trying to vibe out this beautiful little feature right here, generate a level and then I want to be able to see the level and have it generate the exact same every single time.
[05:33] And I want to be able to have all the different display tiles display the exact same way and to have the different height offsets and everything because, you know, some of the tiles are a little bit higher than others.
[05:42] Some are a little bit lower, like this one's lower than that one.
[05:44] Like actually see all the differences in tile heights and make sure that we're still rendering everything the same way.
[05:50] And I'm using all the different tiles, right?
[05:52] Like here's the super green one all the way down to the super red ones.
[05:55] Anyways, it's kind of fun, you know?
[05:57] And so that way I can actually add this to a demo and I can start adding say towers or people walking through.
[06:03] And that way it should always produce the same walk, the same towers, the same shots because the game should be deterministic, which means that I should be able to have demos actually walking and doing everything and it should not break.
[06:19] And if anything breaks, I should be able to flip on logging if I've done this all correctly and be like, yo, yo, definitely not fable because yo, fable, you dead,
[06:28] but not fable.
[06:29] Why don't you go through and just tell me what's wrong?
[06:32] Like read the logs, understand the pixel differences between the two images and just tell me what changed.
[06:38] And hopefully that means if I make any sweeping changes, I should be able to quickly understand what went wrong.
[06:43] And the nice part is when I have decided that I have made some changes and I want to update all of my stuff, I can just go odin run dot, oh, not that.
[06:52] There we go.
[06:54] Demo equals test, save.
[06:56] And by doing that, it's going to save all new goldens.
[07:00] And by saving all new goldens, I now can make sure that I'm producing the same image or the new updated image.
[07:07] Okay, that's all I really wanted to talk about this time.
[07:09] I'm hoping that next week I should be able to start getting into tower placement and enemy movement is kind of my goal is to have enemies walk along the path, have towers be placed and to be able to fire out arrows.
[07:21] So I actually have cards, tower, kill enemies.
[07:25] That might be a little too ambitious.
[07:26] I'll probably pull it back a little bit and just have cards, towers, next level, right?
[07:32] Because if I can at least get to that point, then, you know, we're getting into some pretty serious progress at this point.
[07:39] And of course, the most useless of all measurements, but I thought I'd let you know we're up to 13,000 lines of code.
[07:44] Yikes.
[07:44] Okay, I know I'm no Gary Tan.
[07:46] I'm not producing 30,000 a day.
[07:49] Okay, I'm producing like 1,000, 1,500 a day.
[07:52] I know.
[07:52] Arms, weak.
[07:54] Palms, unsteady.
[07:55] Mom's spaghetti.
[07:56] All right, hey, the name is the Primogen.