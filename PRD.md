# PRD — Todo App (Agent Build Task)

## How to read this
You are an autonomous coding agent. This spec is complete — **do not ask
questions**; where unspecified, pick the simplest option. A hidden test suite
drives the app through the **Interface Contract (§4)**; those `data-testid`s and
behaviors are non-negotiable. Time, tokens, and quality are measured externally,
so be efficient and **add nothing outside this spec**.

## 1. Objective & output
A Todo app delivered as a **single self-contained `index.html`** that runs by
opening the file directly in a browser (`file://`) — **no build step, no server,
no npm, no network requests**. All HTML, CSS, and JavaScript inline in that one
file, **vanilla JS only** (no libraries, no CDN). The user can add, complete,
filter, and delete tasks, and the list survives a reload.

## 2. Features (each independently testable; "active" = not completed)
- **FR1 Add** — typing text and clicking the add control, **or** pressing
  `Enter` in the input, appends a todo to the end of the list.
- **FR2 Reject empty** — empty/whitespace-only input adds nothing; text is
  trimmed before storing.
- **FR3 Clear input** after a successful add.
- **FR4 List** — each todo shows its text, a completion toggle, and a delete control.
- **FR5 Toggle** — flips completion (and back); state reflected in the DOM (§4).
- **FR6 Delete** — removes the todo permanently.
- **FR7 Filter** — All / Active / Completed control which todos are visible;
  default **All**.
- **FR8 Active count** — a live count of active todos updates on every change.
- **FR9 Clear completed** — removes all completed todos, leaving active ones.
- **FR10 Persist** — saved to `localStorage`; reload restores the exact list and
  completion states.

## 3. Data & persistence
- `localStorage` key: **`todos`**
- Value: JSON array of `{ id: string, text: string, completed: boolean }`,
  `id` unique (e.g. `crypto.randomUUID()`).
- Read on load; write the full array after every change. Missing/invalid value →
  start from an empty list (do not throw).

## 4. Interface contract (REQUIRED — tests match this exactly)

| `data-testid`      | Element            | Behavior                                                            |
|--------------------|--------------------|--------------------------------------------------------------------|
| `new-todo-input`   | text `<input>`     | Where the user types; `Enter` adds the todo (FR1).                 |
| `add-todo`         | `<button>`         | Adds the todo in the input (FR1).                                 |
| `todo-list`        | container          | Holds the rendered items for the current filter.                  |
| `todo-item`        | one per todo       | Wraps a todo; sets attr `data-completed="true"`/`"false"`.        |
| `toggle-todo`      | checkbox `<input>` | Inside its item; `checked` = completed; click toggles (FR5).      |
| `todo-text`        | element            | Inside its item; text content = the todo's trimmed text.          |
| `delete-todo`      | `<button>`         | Inside its item; deletes that todo (FR6).                         |
| `filter-all`       | control            | Filter → All (FR7).                                               |
| `filter-active`    | control            | Filter → Active (FR7).                                            |
| `filter-completed` | control            | Filter → Completed (FR7).                                         |
| `active-count`     | element            | Text content is **exactly** the integer count of active todos (e.g. `2`). |
| `clear-completed`  | `<button>`         | Removes all completed todos (FR9).                                |

Items appear in insertion order; item-level testids repeat once per todo.

## 5. Out of scope (do not build)
Editing todo text · due dates / tags / priorities · reordering or drag-and-drop ·
any backend or network call · accounts · routing · **any external library or CDN**.

## 6. Definition of done
- [ ] Opening `index.html` directly in a browser shows a working app — no build, no server.
- [ ] No external/network requests; works offline from the folder.
- [ ] No console errors on load.
- [ ] Every item in §2 and every row in §4 is satisfied.

## 7. Evaluation (transparency)
Primary: % of hidden tests passing. Also: loads and runs with zero errors;
wall-clock and token usage are recorded externally (reach a passing solution
directly); code quality is scored separately.
