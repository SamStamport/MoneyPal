# MoneyPal Usage Tips & Tricks

## General Usage
- Choose LIVE or SAMPLE mode on first run
- Use SAMPLE mode for testing and experimentation
- Switch between modes using the "Switch DB" button

## Data Entry Tips
- **Date Format**: Always enter dates as mm/dd/yyyy (e.g., 12/25/2024)
- **Amounts**: Use negative values for expenses, positive for income
- **Inline Editing**: Click any cell to edit directly in the table
- **Auto-Save**: Changes save automatically when you click away

## Account Management
- **Bank Account**: Track checking/savings transactions
- **Secured Visa**: Track credit card transactions separately
- **Running Balance**: Automatically calculated for each account

## AI Forecasting
- **Minimum Data**: Need 10+ transactions for Prophet AI forecasting
- **Fallback**: Simple averaging used for smaller datasets
- **Accuracy**: Higher accuracy with more historical data
- **Charts**: Visit `/charts` for visual forecasting
 
Note: The app accepts both `mm/dd/yyyy` and ISO `YYYY-MM-DD` date formats when entering or editing transactions. CSV exports use `mm/dd/yyyy`.

## Performance Tips
- Use SAMPLE mode for development and testing
- Export data regularly using CSV export
- Keep transaction descriptions consistent for better analysis

## Troubleshooting
- **Date Errors**: Ensure mm/dd/yyyy format
- **Missing Data**: Check database mode (LIVE vs SAMPLE)
- **Slow Loading**: Large datasets may take time to process

## Keyboard Shortcuts
- **Enter**: Submit new transaction in input row
- **Tab**: Navigate between input fields
- **Escape**: Cancel inline editing

## Best Practices
- Enter transactions regularly for accurate forecasting
- Use descriptive transaction descriptions
- Review charts page for spending patterns
- Export data before switching database modes

## Data Export
- CSV files use mm/dd/yyyy date format
- Separate exports for Bank Account and Secured Visa
- Includes all transaction details and running balances