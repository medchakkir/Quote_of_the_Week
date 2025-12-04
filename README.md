# Quote of the Week

An automated email service that sends an inspirational quote every Sunday to help start your week with motivation and positivity. This project uses Python to randomly select quotes from a curated collection and sends them via email.

## Features

- Automated weekly quote delivery
- Curated collection of inspirational quotes
- Email delivery system
- Random quote selection
- Runs automatically every Sunday

## Requirements

- Python 3.x
- SMTP access (Gmail SMTP server used in this implementation)
- Required Python packages:
  - smtplib (built into Python standard library)
  - datetime (built into Python standard library)
  - random (built into Python standard library)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/momed-ali01/Quote_of_the_Week.git
cd Quote_of_the_Week
```

2. Configure your email settings:
   - Update the email configuration in `main.py`:
     - `MY_EMAIL`: Your Gmail address
     - `MY_PASSWORD`: Your Gmail app password
     - `RECEIVER`: The recipient's email address

## Usage

The script is designed to run automatically every Sunday. To run it manually:

```bash
python main.py
```

### How It Works

1. The script checks if it's Sunday (weekday == 6)
2. If it is Sunday:
   - Reads quotes from `quotes.txt`
   - Randomly selects one quote
   - Sends the quote via email
3. The email includes:
   - Subject: "Quote of the Week"
   - Body: The selected inspirational quote

### Quote Collection

The project includes a curated collection of over 100 inspirational quotes in `quotes.txt`. Each quote is formatted as:

```
"Quote text" - Author
```

## Setting Up Automated Execution

To run this script automatically every Sunday, you can:

1. Use Windows Task Scheduler
2. Use cron jobs (Linux/Mac)
3. Use a cloud service like AWS Lambda or Google Cloud Functions

## Security Notes

- Never commit your email credentials to version control
- Use environment variables or a configuration file for sensitive data
- Consider using Gmail's App Passwords instead of your main password

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
