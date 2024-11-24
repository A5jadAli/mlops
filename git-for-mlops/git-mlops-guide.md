# Git Commands for MLOps Beginners

Welcome to the Git essentials guide for MLOps practitioners! This README provides a comprehensive overview of Git commands you'll need as you begin your MLOps journey. Git is crucial for version control of your ML code, models, and configurations.

## Initial Setup

### First-Time Git Configuration
```bash
# Set your name and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# View your configuration
git config --list

# Set default branch name to main (Optional)
git config --global init.defaultBranch main
```

## Repository Basics

### Creating and Cloning Repositories
```bash
# Initialize a new repository
git init

# Clone an existing repository
git clone https://github.com/username/repository.git

# Clone a specific branch
git clone -b branch-name https://github.com/username/repository.git
```

## Basic Operations

### Tracking Changes
```bash
# Check repository status
git status

# Add files to staging area
git add filename           # Add specific file
git add .                 # Add all files
git add *.py             # Add all Python files

# Remove files
git rm filename          # Remove file from Git and workspace
git rm --cached filename # Remove file from Git only
```

### Committing Changes
```bash
# Create a commit
git commit -m "Your commit message"

# Commit with detailed message
git commit -a -m "Short message" -m "Detailed description"

# Amend last commit
git commit --amend
```

## Working with Remotes

### Managing Remote Repositories
```bash
# Add remote repository
git remote add origin https://github.com/username/repository.git

# View remote repositories
git remote -v

# Change remote URL
git remote set-url origin new-url

# Push to remote
git push origin branch-name
git push -u origin main  # Set upstream and push
```

## Branching and Merging

### Branch Management
```bash
# List branches
git branch              # Local branches
git branch -r           # Remote branches
git branch -a           # All branches

# Create branch
git branch branch-name

# Switch branches
git checkout branch-name
git switch branch-name      # Modern alternative to checkout

# Delete branch
git branch -d branch-name   # Local branch
git push origin --delete branch-name  # Remote branch
```

### Merging
```bash
# Merge branch into current branch
git merge branch-name

# Abort merge in case of conflicts
git merge --abort
```

## History and Logs

### Viewing History
```bash
# View commit history
git log
git log --oneline        # Compact view
git log --graph          # Graphical view
git log --author="name"  # Filter by author
git show <6 digit sha id> # see changes on specific commit
git log -p               # see code changes on commit level

# View specific commit
git show commit-hash
```

## Advanced Operations

### Cherry-picking
```bash
# Apply specific commit to current branch
git cherry-pick commit-hash

# Cherry-pick without committing
git cherry-pick -n commit-hash
```

### Tags
```bash
# Create tag
git tag v1.0.0                    # Lightweight tag
git tag -a v1.0.0 -m "message"    # Annotated tag

# List tags
git tag

# Push tags
git push origin v1.0.0            # Push specific tag
git push origin --tags            # Push all tags
```

### Stashing
```bash
# Stash changes
git stash save "message"
git stash pop                     # Apply and remove stash
git stash apply                   # Apply but keep stash
git stash list                    # List stashes
```

## MLOps-Specific Best Practices (Optional)

### Large File Handling
```bash
# Initialize Git LFS for large model files
git lfs install
git lfs track "*.h5"              # Track H5 model files
git lfs track "*.pkl"             # Track pickle files
git lfs track "*.onnx"            # Track ONNX models
```

## Common Workflows

### Feature Branch Workflow
1. Create feature branch:
```bash
git checkout -b feature/new-model
```

2. Make changes and commit:
```bash
git add .
git commit -m "Add new model implementation"
```

3. Push to remote:
```bash
git push -u origin feature/new-model
```

4. Create pull request (on GitHub)

5. After review and approval, merge:
```bash
git checkout main
git pull origin main
git merge feature/new-model
git push origin main
```

## Troubleshooting

### Undo Changes
```bash
# Discard changes in working directory
git checkout -- filename

# Reset staging area
git reset HEAD filename

# Reset to specific commit
git reset --soft HEAD~1   # Preserve changes in staging
git reset --hard HEAD~1   # Discard changes
```

### Resolve Conflicts
1. When conflicts occur:
```bash
# Identify conflicting files
git status

# Resolve conflicts in files manually
# Look for conflict markers (<<<<<<, =======, >>>>>>>)

# After resolving
git add resolved-file
git commit -m "Resolve merge conflicts"
```

Remember to:
- Write clear, descriptive commit messages
- Commit frequently with logical units of change
- Use branches for new features/experiments
- Keep your repository clean and organized
- Regular push/pull to stay synchronized with team

This guide covers the essential Git commands for MLOps. As you progress, you'll discover more advanced features and develop workflows that best suit your projects.
