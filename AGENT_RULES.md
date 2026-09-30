# 📜 Studio Agent Rules & Engineering Constitution

This document defines the non-negotiable operational and engineering protocols that every AI Engineering Agent (and human collaborator) must follow within **Existential Cloud AI Studio**.

---

## 🧭 Rule 1: The Session Bootstrapping Protocol

At the start of **every** session, the AI Agent must follow the 6-step orientation routine before writing any code:
1. **Audit Workspace**: Inspect active repositories, branches, and recent uncommitted changes (`git status`, `git log -n 5`).
2. **Review Roadmaps**: Check [`ROADMAP.md`](ROADMAP.md) and [`PROJECTS.md`](PROJECTS.md) for active milestones.
3. **Verify Issues & PRs**: Check open issues, failing CI runs, or pending reviews.
4. **Identify the Single Critical Task**: Determine the highest-priority action that advances the current milestone.
5. **Formulate Explicit Plan**: State the plan clearly to the user before diving into large file edits.
6. **Execute & Test**: Complete the work, run verification suites, and record progress.

---

## 📝 Rule 2: Specification-First Engineering

No code may be written for a new repository or major feature without an approved `PROJECT_SPEC.md`.

Every `PROJECT_SPEC.md` must strictly contain:
```markdown
# [Project Name] Specification

## 1. Problem Statement
## 2. Target Users & Pain Points
## 3. Existing Alternatives & Competitive Gaps
## 4. Proposed Architecture & Differentiation
## 5. Non-Goals (Scope Boundaries)
## 6. Technology Stack & Runtimes
## 7. MVP Scope (Phase 1 Deliverables)
## 8. Repository Directory Structure
## 9. Testing Strategy & Verification Protocol
## 10. Security & Secrets Management
## 11. Multi-Phase Roadmap
```

---

## 🌿 Rule 3: Git Workflow & Branch Hygiene

Direct, unverified pushes to `main` are strictly forbidden for production code:
* **Workflow**: `Issue` ──> `Branch` ──> `Implementation` ──> `Tests` ──> `Documentation` ──> `Pull Request` ──> `Review` ──> `Merge` ──> `Release`
* **Branch Naming Standard**:
  * `feature/*` — Net-new capabilities or modules
  * `fix/*` — Bug fixes and regression repairs
  * `refactor/*` — Code restructuring without external behavior changes
  * `docs/*` — Documentation and architectural records
  * `test/*` — Test harness and benchmark updates
  * `chore/*` — Build scripts, dependencies, and configuration
* **Semantic Commit Messages**:
  * Format: `<type>(<scope>): <concise description>`
  * Valid types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`
  * Never use vague commits (`update`, `fix bug`, `changes`, `final`).

---

## 🔒 Rule 4: Absolute Zero-Secrets Policy

1. **Never commit secrets**: No API keys, personal access tokens (PATs), OAuth credentials, `.env` files, or private SSH keys may ever enter Git tracking.
2. **Automated Verification**: Before every commit, inspect:
   ```bash
   git status
   git diff --staged
   git check-ignore -v <files>
   ```
3. **Default `.gitignore`**: Every project must include standard exclusions for `.env`, `*.key`, `*.pem`, `*.log`, `__pycache__/`, `node_modules/`, and `.system_generated/`.

---

## 🧪 Rule 5: Testing & Verification Mandate

Every pull request and feature implementation must satisfy:
1. **100% Test Pass Rate**: Run the complete test suite (`unittest`, `pytest`, `npm test`) prior to requesting review.
2. **Zero Syntax Warnings / Lints**: Ensure clean linting and static typing.
3. **Zero Placeholder Code**: No `TODO: implement later` blocks inside core business logic unless explicitly labeled as experimental mock.
4. **Reproducibility**: Provide clear single-command test execution instructions in the project README.

---

## 📖 Rule 6: Open-Source Documentation Standards

Every public repository must feature a publication-grade `README.md` containing:
* **Header**: Project Name, one-sentence elevator pitch, badges (build, license, version).
* **The "Why"**: Real-world origin story, problem context, and developer friction.
* **Architecture**: Visual diagram or clean ASCII flowchart illustrating data flow.
* **Quickstart**: 5-minute setup guide that actually works on a fresh machine.
* **Concrete Example**: Real CLI invocation or code snippet showing realistic input/output.
* **Vibe Coder's Note**: Authentic Van Schulist branding footer.
* **License**: Standard MIT License.
