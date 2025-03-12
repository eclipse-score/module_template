# DO NOT USE

⚠️ This repo is not working yet! It's not that it's incomplete. It doesn't even work yet! ⚠️

---

# C++ & Rust Bazel Template Repository

This repository serves as a **template** for setting up **C++ and Rust projects** using **Bazel**.
It provides a **standardized project structure**, ensuring best practices for:
- **Build configuration** with Bazel.
- **Testing** (unit and integration tests).
- **Documentation** setup.
- **CI/CD workflows**.
- **Development environment** configuration.

The template includes a **basic "Hello World" example** for both **C++ and Rust**, making it **buildable out of the box**.

---

## 📂 Project Structure

| File/Folder           | Description |
|-----------------------|-------------|
| `README.md`          | Short description & build instructions |
| `src/`               | Source files for the module |
| `tests/`             | Unit tests (UT) and integration tests (IT) |
| `docs/`              | Documentation (Doxygen for C++ / mdBook for Rust) |
| `.github/workflows/`  | CI/CD pipelines |
| `.vscode/`           | Recommended VS Code settings |
| `.bazelrc`, `MODULE.bazel`, `BUILD` | Bazel configuration & settings |
| `LICENSE.md`         | Licensing information |
| `CONTRIBUTION.md`    | Contribution guidelines |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/eclipse-score/YOUR_PROJECT.git
cd YOUR_PROJECT
```

### 2️⃣ Build the Project
#### C++
```sh
bazel build //...
```
#### Rust
```sh
bazel build //rust/...
```

### 3️⃣ Run the Example
#### C++
```sh
bazel run //src:main
```
#### Rust
```sh
bazel run //rust:main
```

### 4️⃣ Run Tests
```sh
bazel test //tests/...
```

---

## 🛠 Tools & Linters

The template integrates **tools and linters** from **centralized repositories** to ensure consistency across projects.

- **C++:** `clang-tidy`, `cppcheck`, `Google Test`
- **Rust:** `clippy`, `rustfmt`, `Rust Unit Tests`
- **CI/CD:** GitHub Actions for automated builds and tests

---

## 📖 Documentation

- A **centralized docs structure** is planned.
