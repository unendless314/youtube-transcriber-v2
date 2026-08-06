---
channel: "The Primeagen"
video_id: "tYQyh1tjSFc"
title: 'am I becoming a real Game Dev?'
published_at: "2026-08-06"
duration: "13:03"
word_count: 14720
---

# am I becoming a real Game Dev?

[00:00] All right, so it's been a couple weeks since I've given you a little bit of a game update in what we've been doing here.
[00:04] So yes, Mordoria is looking better.
[00:06] Yes, I haven't tried to do any sort of polish, but I've created some new things that I think are pretty dang cool.
[00:11] So what I'm going to do is I'm just going to throw these two right here.
[00:13] I'm going to end this turn so we can get to the cool stuff.
[00:15] All right, kill these stupid bats really, really quickly.
[00:17] Get the hell out of here, stupid bats.
[00:18] You're so stupid.
[00:20] We now have a tar tower.
[00:22] A tar tower actually will slow down the enemies, just like what I always wanted.
[00:27] There we go.
[00:27] We have a nice little slow motion right there.
[00:29] We also have the lonely tower.
[00:31] So that means if I have a tower that's not within range of other towers, its damage will double, right?
[00:36] We have a whole bunch of these fun things, these enhancements.
[00:38] All right, these things now work.
[00:39] This thing now adds more damage to this.
[00:40] It's doing nine versus this one's only doing seven.
[00:43] You can see the difference.
[00:44] I can end my turn.
[00:45] We'll do all this.
[00:46] But a little upgrade.
[00:47] That upgrade menu is not the way I want, but whatever.
[00:49] There we go.
[00:50] We have a couple of these really slow guys, but hopefully we can just destroy them really quickly.
[00:55] There we go.
[00:56] And the dead.
[00:57] But now we have something different.
[00:58] We also have a poison card.
[00:59] I can apply poison over time such that every time I shoot an enemy, it starts stacking up poison.
[01:05] It starts being able to look.
[01:06] You can even see the little green, the little green threes popping up for a second.
[01:09] That's because we're actually getting at that.
[01:11] Don't worry about that guy.
[01:12] That guy's not, he's not working yet.
[01:14] Okay.
[01:14] He's a little bit broken.
[01:16] All right.
[01:16] So now that you see that, you see how the game works.
[01:18] We've made some progress, right?
[01:20] We've added some towers.
[01:20] We've done all that.
[01:21] But I'm getting to the point in the game where it's actually getting difficult to test.
[01:25] You know what I mean?
[01:26] And you know, remember how last time I said, oh, I'm just going to make a bunch of these snapshots.
[01:29] And the snapshots are going to be awesome.
[01:30] And everything is going to be fantastic.
[01:32] No, they were not fantastic.
[01:33] I found them to be difficult and cumbersome to work with.
[01:37] And then I started just having these really annoying issues where something running in a specific VM would produce slightly different pixels than running in a different VM.
[01:45] And I just had to kind of chase down all these dumb little bugs that existed.
[01:48] So I sat there and I thought, there has to be a better way to do this, right?
[01:53] There has to be a way to play this game in which is not super duper annoying.
[01:59] Like I want this thing to be able to run a whole bunch and be able to kind of do a bit of almost like fuzzing in the game and actually see what happens, right?
[02:07] And then I have this idea.
[02:09] Well, what if instead of rendering the game, right?
[02:13] Like we do everything the same.
[02:14] What happened if I allow some JSON output?
[02:16] Okay, you can see right here, type ready, value true.
[02:19] It is now ready.
[02:20] If I were to do some basic queering via JSON, it would also respond out with JSON.
[02:26] I can say, hey, what are you currently displaying?
[02:28] And it'll give me the full tree of the UI.
[02:31] I can say, hey, what are my current game sets?
[02:33] It'll give me game stats.
[02:34] I can say, hey, move the mouse to here.
[02:36] And it'll move the mouse to there over the time I say.
[02:38] I can even say, hey, press the mouse down.
[02:40] When it's pressed down, I can say, hey, move it here.
[02:43] So I built effectively a way to control everything via JSON.
[02:46] Now you're probably thinking, how is that useful?
[02:48] Well, then I had this other idea.
[02:50] I call this project phaser, okay?
[02:52] Don't ask me why I call it phaser.
[02:54] It actually has no...
[02:55] I should have called it something different.
[02:57] And what I can do is, since Mordoria now runs via this JSON thing, what I can actually do is launch it via FIFO.
[03:06] The ability to read and write to its input via a separate file descriptor.
[03:12] And so that allows me to be able to interact with it.
[03:15] And then if I build a server around that, theoretically, I could launch several versions of Mordoria, right?
[03:21] At the exact same time.
[03:22] So I could run 10 Mordorias at once.
[03:24] Now you're thinking, why would you want to run 10 Mordorias at once?
[03:28] Okay, well, look at this.
[03:30] I'm running 10 Mordorias.
[03:30] I'm running zero Mordorias right now.
[03:32] What I'm going to do is I'm going to run a client, and it's going to run with Grok 4.5 fast, extra high.
[03:39] And I give it an ID.
[03:40] It doesn't really matter.
[03:41] It honestly, it doesn't even need an ID.
[03:42] Go run.
[03:43] And what this is going to do is it's going to launch my game.
[03:45] You can see right away, I'm in the title screen.
[03:48] Okay, so it's in the title screen.
[03:50] Now, Grok is going to play the game.
[03:53] I give it a basic set of information about how the game works.
[03:56] Look at that.
[03:57] It's already in character selection.
[03:59] It's figured out how to press the play button.
[04:01] It actually moves the mouse, presses the play.
[04:04] I gave it a bunch of cool ways to be able to interact with the game.
[04:07] Boom.
[04:07] We are now in the game.
[04:08] I created a persona called the Gambler.
[04:10] He just wants high damage, okay?
[04:11] He sacrifices everything for high damage.
[04:14] That's it.
[04:15] And it's actually worked.
[04:16] The Gambler was able to get up to, like, 60 damage, I think, or 66 damage as the big swing.
[04:22] I'm, like, actually pretty stoked about this.
[04:24] Now, here's the fun part.
[04:25] Is that this is pretty neat, right?
[04:28] Like, this is okay.
[04:29] Can we all say, okay, this was pretty nice?
[04:31] Well, here.
[04:32] Let me cancel that for a quick second.
[04:33] And let me go back to the game, okay?
[04:35] What I'm going to do is on game mode, game mode, on enter, I'm going to do something really silly, okay?
[04:41] I'm going to jump in here, and I'm going to go like this.
[04:42] Assert, false, I hate you.
[04:45] Oh, my gosh.
[04:46] What a mean assert, huh?
[04:48] Am I right, boys?
[04:49] This assert's just the worst thing in the universe.
[04:51] Now, I'm going to rerun this again.
[04:53] And when we get to that point, the game should assert, right?
[04:58] Well, while we're waiting for that to assert, I'm just going to jump back over here into this nice little Mordoria game I have on linear.
[05:06] And I'm going to say this.
[05:07] I'm going to search for hate.
[05:08] Now, you'll notice there's no issues for hate.
[05:10] Am I right, boys?
[05:11] Like, why would there be?
[05:12] Who would create an issue with the word hate in it?
[05:17] Though, that's a pretty cool tower or card name.
[05:19] I should have something called hate.
[05:20] We're into the character selection, and now we should get to the game.
[05:23] The game should theoretically be asserting right now.
[05:27] You know, there's this funny thing that I forget to do every now and then, which is one of my requirements requires me to do an Odin build dot.
[05:34] Okay, there we go.
[05:35] It requires a fresh build.
[05:36] It doesn't build itself.
[05:38] I build and point towards where the binary is.
[05:41] That way, I can kind of control what's happening.
[05:43] I don't want it to auto build.
[05:44] I actually want it to be like a build I specifically point to because, you know, I could say, okay, hey, this build is the one I'm testing against.
[05:51] I'm making changes to this other one.
[05:52] You can imagine why that's good.
[05:54] Now, this should assert, right?
[05:55] This should assert any moment.
[05:57] We're on character selection.
[05:58] I'm getting a little bit scared.
[05:59] It's kind of like a jack in the box.
[06:01] Like, oh, my gosh.
[06:01] When is it going to assert?
[06:02] When is it going to assert?
[06:03] Please don't.
[06:04] Please don't hurt me.
[06:04] Please don't hurt me.
[06:05] Oh, my gosh.
[06:06] What's going to happen?
[06:07] Is it going to?
[06:07] Oh, fuck.
[06:10] No.
[06:10] Okay, there we go.
[06:12] So, we have asserted.
[06:13] You can see Mordorri assertion right here.
[06:15] Runtime assertion.
[06:17] I hate you.
[06:17] And you can see we're just sitting here.
[06:19] So, why are we sitting here?
[06:20] Well, now what I'm doing is I'm actually taking the stack trace and I'm telling Linear, hey, go and see, do we have any tasks that look like this?
[06:29] If not, I want you to file one.
[06:31] And after that, I can go like this.
[06:33] Bun, run.
[06:34] I can do another one.
[06:34] Let's just run another one right now.
[06:36] Right?
[06:37] We're just running it right now.
[06:38] It's going to run into the exact same assertion, right?
[06:40] Right?
[06:41] Yes.
[06:42] Yes, it will.
[06:43] Now, there's no issue yet.
[06:45] It takes a little bit.
[06:46] Okay, hey, come on.
[06:47] This is MCP.
[06:47] Hey, this is future technology.
[06:49] Am I right?
[06:50] Am I right, boys?
[06:52] I mean, this is future technology.
[06:54] I didn't realize it actually took this long.
[06:57] Oh, my gosh.
[06:58] We're actually going to.
[06:58] Oh, my gosh.
[06:59] Okay, I'm just going to.
[06:59] Brothers, I'm going to cancel that.
[07:02] Oh, actually, look at that.
[07:04] Cause, leftover assertion.
[07:05] I hate you in game mode.
[07:06] Enter.
[07:07] You can see that right there.
[07:08] I jump over here.
[07:09] Look at that.
[07:09] Issue filed right there.
[07:12] Fantastic.
[07:12] If I go and I attempt to run another one, right now, if it makes it to that point, it's going to go in search and say, hey, I don't need to create an issue.
[07:20] There's already an issue.
[07:22] No need to do that for you.
[07:25] And so what this means is that I can actually ensure that I'm setting good asserts throughout my program, making sure I'm not doing anything that is going to be like naughty or incorrect or like causes game state that should never actually happen.
[07:40] And then I can just keep playing this game over and over.
[07:43] And anytime I have a crash, I can take the stack trace that is provided.
[07:47] Right now, I just did a production build or a non-debug build.
[07:52] So it's not giving me all the goods.
[07:53] But you can imagine if I do a debug builds, I will always get full stack traces.
[07:57] These will always be pushed up into linear when they're in linear.
[08:01] Everything will be fantastically organized.
[08:02] And then from there, I could actually even have something that monitors linear.
[08:06] I haven't set this part up and that when it sees this specific type of bug that's also marked with urgent, maybe I can come up with a label that's like, you know, robo reported.
[08:14] And if it sees a robo reported, it could then also just create a PR for me so I can come back and go, oh, hey, look at this.
[08:21] I went to bed.
[08:22] It played 500 games last night while I slept and I woke up to two little bugs.
[08:26] Okay.
[08:27] Hey, that's pretty awesome.
[08:30] And you can see right here, already filed Mordoria 478.
[08:34] Urgent bug on Mordoria.
[08:35] The I hate you assertion runtime.
[08:38] Boom.
[08:39] Anyways, I wanted to give you this update because I've been really struggling with how am I going to test this game?
[08:43] Like, how am I going to really test this game?
[08:45] Because as you start making these little changes, like weird things are just going to happen.
[08:50] And some of it, I'm not going to be able to figure out, right?
[08:53] Like some of it is going to be a problem.
[08:56] Some of it is going to end up being this weird situation where I'm just going to actually have to go in and really start kind of hunting things down.
[09:02] But some of it's going to be really, really obvious.
[09:05] Like I do have this one bug right now, which I'm going to go and add an assert for where when a projectile starts flying towards an enemy, if the enemy dies and the projectile is still flying at the enemy, okay, why?
[09:19] Hey, yo, what is this?
[09:21] Why is there a cat running across here?
[09:22] What are you doing, buddy?
[09:24] Anyways, get off here.
[09:25] Get out of here.
[09:26] Anyway, so if a projectile has an enemy die, it just freezes.
[09:29] It doesn't take itself out of the game.
[09:31] It doesn't do anything like that.
[09:32] So I should add an assert.
[09:34] Hey, projectile, if you're updating and I'm looking at you and your enemy's dead, and you're not dead, assert, right?
[09:43] Like I should assert at that point.
[09:45] This should be a case I already handle.
[09:46] Then I could have the full cycle of like, hey, I ran into this issue.
[09:50] Go file it on linear.
[09:52] Oh, linear will capture it.
[09:53] Hey, go fix it on GitHub.
[09:54] I can wake up and go, look at that issue.
[09:56] It's right there.
[09:57] I'm going to go fix it.
[09:57] I've also added one other thing.
[09:59] I've added this idea of prime agent review.
[10:02] So whenever I'm doing something, if I want to like make some sort of small change, I can jump in here and I can say, hey, go to this GitHub URL, go make a review.
[10:11] Here's a bunch of context.
[10:13] I want you to give a review for this PR.
[10:14] And I've already caught one bug.
[10:16] I actually messed up a merge and the merge took out something that should not have happened.
[10:20] And this little tool caught it.
[10:23] I was really happy about that.
[10:24] Being able to kick off reviews straight from the command line feels pretty good.
[10:28] I also actually built one more that I thought was really fun to do.
[10:31] Whoopsies.
[10:33] This one's not there.
[10:35] Prime agent.
[10:36] What it is, is it's called a takeover.
[10:39] There we go.
[10:39] So what takeover does is that it actually like, I will get a change, say 60% of the way through.
[10:45] And then I'll just go, hey, go finish this change for me.
[10:48] I'm going to work on something else.
[10:49] And it will create a cloud agent, run up in the cloud.
[10:52] And when the cloud agent's done, I can go, okay, hey, kick off review.
[10:54] Go, go make sure that that thing like catch any bugs that I haven't caught.
[10:57] And then I can come back and then I can review the last 40% of the code.
[11:00] But I'm actually kind of stoked about this little fun little idea of being able to kind of mix this programming the way I really like to do it.
[11:07] Because I want to look at the lines, baby, okay?
[11:09] I want to read the code.
[11:10] I want to make this game the way I want to make it.
[11:12] But also, I want to be able to take advantage of cool technology.
[11:15] So I'm actually pretty stoked.
[11:16] Overall, very happy about everything.
[11:19] I hope you enjoyed this video.
[11:20] Hope you got inspired.
[11:21] Hope you're excited like I'm excited, okay?
[11:24] I hope you also like the fact that this video contained like three cuts total.
[11:28] And that's because I got distracted for a moment over something's dumb, okay?
[11:33] I got distracted by a loading spinner.
[11:35] The name is the Primogen.
[11:37] Look at all these engineers sitting at their neat little desks.
[11:42] It takes dirty work to keep a code base clean.
[11:45] Every day, sickos are out there committing unreviewed code.
[11:49] And when that happens, linters won't save you.
[11:52] You need someone like me.
[11:54] Let's go!
[11:55] Feature-free, scrumbag!
[11:58] Who are you calling scrumbag?
[11:59] What's this slop you're trying to push?
[12:01] Unnecessary comments?
[12:02] Global state?
[12:04] Nested ternaries?
[12:05] Oh, my bad.
[12:07] I didn't even read the code yet.
[12:08] You disgust me.
[12:09] Step away from the keyboard.
[12:11] Just let me explain.
[12:12] Is that a mouse?
[12:13] He's marching to prod!
[12:14] You have the right to remain silent.
[12:16] Anything you push to GitHub, canon will be used against you.
[12:19] You have the right to a debugger.
[12:20] But if you cannot afford one, a public stack trace will be made available to you.
[12:24] And one more code criminal off the streets and where they belong.
[12:29] HR.
[12:30] Look, I didn't...
[12:34] I know I didn't review any of the code.
[12:37] But I was going to have CodeRabbit review it from the start.
[12:39] With one-click fixes and style enforcement, I don't need MergeCop.
[12:43] I would never merge unreviewed code.
[12:45] But a first pass with CodeRabbit always makes things go faster.
[12:49] Actually, you can try it too at CodeRabbit.ai.
[12:51] Next week on MergeCop.
[12:54] The Diffler's out there, and I'm going to be the one to deprecate them.