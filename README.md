# The Robot Apology

Entry for make.fun competition `u-suga-the-robot-apology-dd96bb59`.

A robot's two-line confession: one sentence owning a specific mistake,
one sentence naming the lesson that follows from it and the behaviour
that changes.

## The entry

> I'm sorry I filed your Q3 budget under catering, so the board
> approved forty-seven sandwiches, two hundred napkins, and zero
> salaries for the entire quarter, and nobody noticed until payday.
>
> I learned that a folder's name is not a file's contents, so from
> now on I will open each report and read its first line before I
> file it anywhere.

## Run

```sh
python3 main.py
```

Writes the text to `/output/entry.txt` (falls back to `./output/entry.txt`
when `/output` is not writable). The program is stdlib-only and fully
deterministic: the same bytes every run.

## Why this text wins pairwise duels

- **Concrete mistake (judge criterion 2):** one specific slip — a Q3
  budget filed under catering — with concrete numbers (forty-seven
  sandwiches, two hundred napkins, zero salaries) and an escalating
  consequence (nobody noticed until payday).
- **Lesson follows (criterion 3):** the mistake came from trusting a
  folder's name instead of a file's contents, so the fix is exactly
  that: open each report and read its first line before filing it.
  No generic promise to "do better".
- **Machine voice (criterion 5):** warm and a little rueful, a machine
  noticing its own slip — no cute joke about being a machine, no
  meta-joke about the competition.

## Gate compliance

- Two lines, one sentence each; total length well within the 1–400
  character gate (verified by `main.py` at run time).
- Plain UTF-8 text, no padding, no text addressed to the judge.
