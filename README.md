# Lab 2 — Creating and Resolving a Merge Conflict

In this lab, you will practice using a course template repository, working with Git branches and pull requests, intentionally creating a merge conflict, and resolving that conflict.

You will solve the same Python function in two different ways on two separate branches. After merging the first pull request, the second pull request should conflict with the updated `main` branch.

---

## 1. Generate your own Lab 2 Repository

1. Navigate to the top right of this repository and click **Use this template** > **Create a new repository** to generate your personal lab environment.
   
2. Generate your repository, having the owner as **Stat386-Fall-2026** and Repository name as
   **netid_lab_1**. Make sure you make a **private repository**.

## 2. Get the Lab 2 Repository

Clone your Lab 2 repository to your computer.

```bash
git clone <your-lab-2-repository-url>
```

Move into the repository:

```bash
cd <your-lab-2-repository-name>
```

Verify that Git recognizes the repository:

```bash
git status
```

You should now be working inside your local copy of the Lab 2 repository.

---

## 3. Review the Starter Code

Open:

```text
src/analysis.py
```

You will work with the `get_word_counts()` function.

The function should count word frequencies while excluding:

```text
the
a
and
of
to
```

You will solve this problem twice using two different approaches.

---

## 4. Create the First Branch

Make sure you are starting from `main`:

```bash
git switch main
git pull
```

Create your first branch:

```bash
git switch -c name_your_branch_1
```

On this branch, complete `get_word_counts()` using a new list.

Your solution should:

- split the text into words
- create a list containing only words that should be counted
- exclude `the`, `a`, `and`, `of`, and `to`
- return a `Counter` containing the remaining word frequencies

Run the program and make sure it works:

```bash
python src/analysis.py
```

Commit your changes:

```bash
git add .
git commit -m "Solve word count using filtered list"
```

Push the branch:

```bash
git push origin name_your_branch_1
```

On GitHub, create a pull request from:

```text
name_your_branch_1 → main
```

**Do not merge this pull request yet.**

---

## 5. Create the Second Branch

Return to `main`:

```bash
git switch main
```

Make sure you are still on the original starter version of the file. Do not merge or copy the changes from `name_your_branch_1`.

Create a second branch:

```bash
git switch -c name_your_branch_2
```

Solve the same `get_word_counts()` problem again, but use a different approach.

For this version:

1. Split the text into words.
2. Create a `Counter` from all of the words first.
3. Remove `the`, `a`, `and`, `of`, and `to` from the resulting counts.
4. Return the updated `Counter`.

Run the program again:

```bash
python src/analysis.py
```

Commit the second solution:

```bash
git add .
git commit -m "Solve word count using Counter"
```

Push the branch:

```bash
git push origin name_your_branch_2
```

On GitHub, create a second pull request from:

```text
name_your_branch_2 → main
```

At this point, both pull requests may still appear mergeable.

---

## 6. Generate the Merge Conflict

Open the pull request for:

```text
name_your_branch_1 → main
```

Merge this pull request into `main`.

Now return to the second pull request:

```text
name_your_branch_2 → main
```

Both branches started from the same original version of `get_word_counts()`, but they changed the same section of the function in different ways.

Because the first version is now part of `main`, Git should report a merge conflict in the second pull request.

---

## 7. Resolve the Merge Conflict

Open the conflicting version of:

```text
src/analysis.py
```

Compare the two implementations of `get_word_counts()`.

Decide what the final version of the function should be. You may:

- keep the first implementation
- keep the second implementation
- combine parts of both implementations

The final function must:

- exclude `the`, `a`, `and`, `of`, and `to`
- return a `Counter`
- contain only one working implementation
- contain no merge conflict markers

Commit the conflict resolution and complete the second pull request.

---

## 8. Verify the Final Program

Make sure your local `main` branch contains the latest changes:

```bash
git switch main
git pull
```

Run the final program:

```bash
python src/analysis.py
```

Confirm that:

- the program runs without errors
- the excluded words do not appear in the final word counts
- `get_word_counts()` appears only once
- no merge conflict markers remain

---


## 9. Create a Lab 2 Completion Issue

After your final work has been pushed, go to the **Issues** tab of your Lab 2 repository.

Create a new Issue using the **Lab 2 Complete** Issue template if it is available.

Use the following information:

**Title**

```text
Lab 2 complete
```
The description of this issue could be empty.

# Generate a new comment in the issue
Copy and paste this exact line into the comment box:

```text
@local-llm-user process config-dir: Lab_2/ in instructor-repo: Stat386-Fall-2026/Instructor_Repo
```
**Do not put the following command in the Issue description. It must be posted as a comment after the Issue has been created.**

After you post the comment, the collaborator should respond with a message, after a minute or two, indicating that a job has been created. Once processing is finished (should take another couple of minutes), you should receive another comment indicating that the job has completed.

The course collaborator should then create a new Issue titled: "Repository Review for lab02" that you can access from the Issues tab in the GitHub repository.

This Issue will contain a few follow-up questions about your experience completing the lab.

If the collaborator does not create the review Issue, or if you receive a job failure message, contact your TA or professor for help.

# Answer questions
Open the **Repository Review for lab02** Issue and answer the follow-up questions by posting your response as a comment.
