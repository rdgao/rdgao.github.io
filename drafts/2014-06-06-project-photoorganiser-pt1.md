---
title: 'Project: PhotoOrganiser Pt.1'
categories: []
tags: []
status: draft
type: post
published: false
meta: {}
---

I will have finally caught up on my weekly duties after this post (week 6?),
even though I'm totally about to cheat and not write about anything.

So the back story is that, after roughly 2 years of taking photos at an
ungodly pace using my expansive array of photo-taking thingies, I now run into
the problem of organizing and making sense of some-5000 photos. I started
binning them manually into events, and although it's led me through quite the
trip down memory lane, let's be honest here: ain't nobody got time for that.
So, as any self-respecting (read: lazy) engineering graduate would do, I
figured I could write some code for it. I could have done this whole thing
-organization, analysis, and the whole 9 yard- in about 2 hours on MATLAB. But
I've been meaning to, for the Nth time, pick up my Python for a while, so I
figured it might be fun to learn it on the fly. After all, this agrees with my
recent realization that I absolutely can't learn or remember anything without
actually using it. Not that I was going to just read a Python book, but real
life struggles beat example exercises any day.

Anyway, here it is: [PhotoOrganizer](https://github.com/rdgao/PhotoOrg). It's
really rather rudimentary right now, all it's doing is finding {jpg, bmp, png,
etc} files in a folder and renaming them by their last-modified time
(yyyy_mm_dd_hr_mi_se), which, conveniently enough for me, happens to be the
time the photos are taken using my {iPod, GalaxyS3, Nexus7, camera}. No
guarantees that it's the same for other devices though. Also,

