# Contributing to Strix

Thank you for your interest in contributing to Strix! This guide will help you get started with development and contributions.

## 🚀 Development Setup

### Prerequisites

- Python 3.12+
- Docker (running)
- [uv](https://docs.astral.sh/uv/) (for dependency management)
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/usestrix/strix.git
   cd strix
   ```

2. **Install development dependencies**
   ```bash
   make setup-dev

   # or manually:
   uv sync
   uv run pre-commit install
   ```

3. **Configure your LLM provider**
   ```bash
   export STRIX_LLM="openai/gpt-5.4"
   export LLM_API_KEY="your-api-key"
   ```

   > **Personal note:** I've been using `anthropic/claude-opus-4-5` locally and it works well for most skill testing. YMMV depending on your API access.
   >
   > For a cheaper alternative during development/testing, `anthropic/claude-haiku-3-5` is noticeably faster and costs a fraction of the price — good enough for iterating on skills before running a full eval with a bigger model.
   >
   > I keep these exports in a local `.env` file and source it with `source .env` — easier than re-exporting every session. Just make sure `.env` is in `.gitignore` (it already is).
   >
   > **Note to self:** On my home machine I also set `export STRIX_TIMEOUT=120` since my internet is flaky — the default 30s timeout causes spurious failures on larger targets.
   >
   > Also found it useful to set `export STRIX_MAX_RETRIES=5` when testing against rate-limited APIs — the default of 3 wasn't enough for burst runs.
   >
   > Setting `export STRIX_LOG_LEVEL=debug` is also handy when a run fails silently — gives you a lot more context on what the agent was doing before it bailed.
   >
   > **Tip:** I alias the full dev invocation in my shell config: `alias strix-dev='source .env && uv run strix'` — saves a lot of typing.

4. **Run Strix in development mode**
   ```bash
   uv run strix --target https://example.com
   ```

## 📚 Contributing Skills

Skills are specialized knowledge packages that enhance agent capabilities. See [strix/skills/README.md](strix/skills/README.md) for detailed guidelines.

### Quick Guide

1. **Choose the right category** (`/vulnerabilities`, `/frameworks`, `/technologies`, etc.)
2. **Create a** `.md` file with your skill content
3. **Include practical examples** - Working payloads, commands, or test cases
4. **Provide validation methods** - How to confirm findings and avoid false positives
5. **Submit via PR** with clear description

## 🔧 Contributing Code

### Pull Request Process

1. **Create an issue first** - Describe the problem or feature
2. **Fork and branch** - Work from the `main` branch
3. **Make your changes** - Follow existing code style
4. **Write/update tests** - Ensure coverage for new features
5. **Run quality checks** - `make check-all` should pass
6. **Submit PR** - Link to issue and provide context

### PR Guidelines

- **Clear description** - Explain what and why
- **Small, focused changes** - One feature/fix per PR
- **Include examples** - Show before/after behavior
- **Update 