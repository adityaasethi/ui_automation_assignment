# TripJack flight-automation Project

Welcome to the TripJack flight-automation Project repository. This repository is intended for internal use by the TripJack Team for flight-automation using Python and Robot Framework.

## Prerequisites

Before you start, ensure you have the following installed and set up:

- **Homebrew**:
  - Install Homebrew, the package manager for macOS:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

- **PyCharm IDE**:
  - Download and install [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/).
  - Avoid installing the `Pop up Plugin`.
  - Install the following plugins via `Settings` → `Plugins` → `Marketplace`:
    - `Intellibot #patched`
    - `Batch Script support`
    - `Robotframework language server`
    - `RobotRunner`

- **Python Interpreter**:
  - Set up Python interpreter with the latest version in PyCharm IDE.

- **Install JSON Library(MAC)**:
  - /Library/Developer/CommandLineTools/usr/bin/python3 -m pip install robotframework-jsonlibrary
- 
## Getting Started

Follow these steps to set up and run the project:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd project-directory
   ```

2. **Install Dependencies**:
   Run the following command in the terminal to install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   ### Install Requirements at Local Machine Core Level
   To install the requirements at the local machine core level, run:
   ```bash
   /Library/Developer/CommandLineTools/usr/bin/python3 -m pip install -r requirements.txt
   ```

## Working with Jira and GitHub

1. **Jira Setup**:
   - Complete the Jira setup for issue tracking and project management.

2. **Creating a New Branch**:
   - If assigned a Jira story, create a new branch from the `dd-final` main branch:
     ```bash
     git checkout dd-final
     git checkout -b feature/<JIRA-ISSUE-ID>-<branch-name>
     ```

3. **Development Workflow**:
   - Make changes, add files to the staging area, and commit with meaningful messages:
     ```bash
     git add .
     git commit -m "Implement feature XYZ: Detailed message"
     ```

   - Push changes to your branch:
     ```bash
     git push origin feature/<JIRA-ISSUE-ID>-<branch-name>
     ```

4. **Code Review and Pull Request**:
   - Notify your Team Lead (TL) for code review.
   - Resolve any conflicts and ensure the branch is ready for merge.
   - Raise a pull request (PR) from your branch into `dd-final/main` branch.

## Running the Automation Process Manually with Github Action

Follow these steps to manually run the automation process and receive the report via email:

1. **Log into GitHub**:
   - Go to your GitHub account and log in with your credentials.

2. **Navigate to Your Repository**:
   - Access your organization's workspace and select the repository for the TripJack flight-automation Project.

3. **Access GitHub Actions**:
   - Click on the "Actions" tab in your repository.

4. **Select the Workflow**:
   - Find and select the workflow named `Robot Framework Tests DD Final` from the "All workflows" section.

5. **Run the Workflow**:
   - Click on "Run workflow" button.

6. **Configure Workflow Options**:
   - In the popup dialog:
     - Choose "Use workflow from" and select the default option.
     - Provide an Email address for notifications (default: `qa-automation@tripjack.com`).
     - Specify Tags Need to Run (default: `all`).
     - Set the Thread Count to run at a time (default: `50`).

7. **Start the Automation**:
   - Click on "Run Workflow" to initiate the automation process.

8. **Monitor Execution and Report**:
   - Monitor the workflow execution status on GitHub.
   - Once completed, the report will be sent to the specified email address.

9. **Review Results**:
   - Review the automation results and any notifications received via email.

Ensure all steps are followed correctly to run and manage the automation effectively.


## License

For Internal team uses only.

### Notes:

- **Replace placeholders** like `<repository-url>`, `<JIRA-ISSUE-ID>`, `<branch-name>`, `[Your Name or Team Contact]`, `[email or contact information]`, and `[License Name]` with actual values specific to your project.
- **Provide detailed instructions** within each section to guide users effectively.
- **Update and maintain** the `README.md` file as the project evolves to keep it relevant and useful.
```

*** Github Actions workflow Information ***

| Workflow name                                   | Team Name                                     | runner              |  actions-runner  |
|-------------------------------------------------|-----------------------------------------------|---------------------|----------------- |
| Automation Team - Manual Run - Flight Automation| Automation Team                               | AWShosted2          |  actions-runner2 |
| Dev Team - Manual Run - Flight Automation       | Dev Team                                      | AWShosted4          |  actions-runner4 |
| Flight Automation Cron All                      | Automation Team                               | AWShosted           |  actions-runner  |
| Flight Automation Mini Regression Suite         | Automation Team                               | AWShosted           |  actions-runner  |
| Manual Team - Manual Run - Flight Automation    | Manual Team                                   | AWShosted5          |  actions-runner5 |
|-------------------------------------------------|-----------------------------------------------|---------------------|----------------- |