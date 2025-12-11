# Quote of the Day

An automated email service that sends inspirational quotes via email. This project uses Python to fetch quotes from an API and sends them via email using Gmail SMTP.

## Features

- API-based quote fetching
- Email delivery system via Gmail SMTP
- Environment variable configuration for secure credential management
- Comprehensive error handling for API and email operations
- Easy to automate with task schedulers

## Requirements

- Python 3.x
- Gmail account with App Password enabled
- API access (quote API endpoint with API key)
- Required Python packages (see `requirements.txt`):
  - `python-dotenv` - For loading environment variables
  - `requests` - For making API calls to fetch quotes
  - `smtplib` - Built into Python standard library for email sending

## Installation

1. Clone this repository:

```bash
git clone https://github.com/<username>/Day.git
cd Quote_of_the_Day
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with the following variables:

```env
API_KEY=your_api_key_here
API_ENDPOINT=https://api.api-ninjas.com/v2/quoteoftheday
SENDER_EMAIL=your_email@gmail.com
RECEIVER_EMAIL=recipient@example.com
SENDER_PASSWORD=your_gmail_app_password
```

**Important:**

- Replace all placeholder values with your actual credentials
- Never commit the `.env` file to version control
- For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password

## Usage

To run the script:

```bash
python main.py
```

### How It Works

1. The script loads environment variables from `.env` file
2. Validates that all required environment variables are present
3. Fetches a quote from the configured API endpoint using the API key
4. Displays the quote in the console
5. Sends the quote via email using Gmail SMTP
6. The email includes:
   - Subject: "Quote of the Day"
   - Body: The fetched quote with author attribution

### Error Handling

The script includes comprehensive error handling for:

- Missing environment variables
- API request failures (network errors, timeouts, HTTP errors)
- JSON parsing errors
- SMTP authentication failures
- General SMTP errors
- Unexpected exceptions

## Setting Up Automated Execution

To run this script automatically on a schedule, you can:

1. **Windows Task Scheduler**: Create a scheduled task to run the script daily
2. **Linux/Mac Cron Jobs**: Add a cron job to execute the script at specified intervals
3. **Cloud Services**: Deploy to AWS Lambda, Google Cloud Functions, or similar services
4. **GitHub Actions**: Set up a scheduled workflow to run the script

Example cron job (runs daily at 9 AM):

```bash
0 9 * * * /usr/bin/python3 /path/to/Quote_of_the_Day/main.py
```

## Security Notes

- **Never commit your `.env` file** to version control - it contains sensitive credentials
- Use Gmail's App Passwords instead of your main account password
- Keep your API key secure and rotate it periodically if compromised
- Consider using a secrets management service for production deployments
- The `.env` file is already included in `.gitignore` (if present) to prevent accidental commits

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
