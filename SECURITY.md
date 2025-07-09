# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in MoneyPal, please report it to our security team at security@example.com. We take all security issues seriously and will respond as quickly as possible to your report.

### Guidelines for Reporting Security Issues

- **Do not** report security issues through public GitHub issues or discussions
- Provide a detailed description of the vulnerability
- Include steps to reproduce the issue
- If possible, provide a proof-of-concept or exploit code

## Security Measures

### Data Protection
- All sensitive data is encrypted at rest and in transit
- Passwords are hashed using bcrypt
- API endpoints use HTTPS with proper TLS configuration

### Authentication
- Secure session management
- Password complexity requirements
- Account lockout after multiple failed login attempts
- CSRF protection

### Dependencies
- Regular dependency updates
- Security patches applied promptly
- Use of trusted packages with active maintenance

## Responsible Disclosure

We follow responsible disclosure guidelines:
1. Report the vulnerability to our security team
2. Allow reasonable time for the issue to be addressed
3. Do not disclose the vulnerability publicly until it has been fixed
4. Work with us to verify the fix

## Security Best Practices for Users

- Use strong, unique passwords
- Enable two-factor authentication when available
- Keep your devices and browsers up to date
- Be cautious of phishing attempts
- Log out after each session, especially on shared devices
