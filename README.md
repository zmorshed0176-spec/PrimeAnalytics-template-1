# PrimeAnalytics AI Agent

An AI-powered website analytics audit tool that automatically analyzes websites, detects CMS platforms, identifies tracking implementations, and generates ready-to-use Google Tag Manager (GTM) containers with conversion tracking setup.

## Features

### 🔍 **Comprehensive Website Analysis**
- **CMS Detection**: Automatically identifies the platform (WordPress, Shopify, Webflow, etc.)
- **Technology Stack Analysis**: Detects frameworks, libraries, and tools
- **Performance Metrics**: Page load time, response time, and technical health checks

### 📊 **Analytics Audit**
- **Current Tracking Detection**: Identifies existing GTM, GA4, Facebook Pixel, and other tracking
- **Privacy Compliance Check**: Detects consent management platforms
- **Tracking Gap Analysis**: Identifies missing or improperly configured tracking

### 🎯 **Conversion Opportunities**
- **E-commerce Tracking**: Identifies purchase funnels, cart abandonment points
- **Lead Generation**: Detects forms, sign-ups, and lead capture opportunities
- **Engagement Events**: Video tracking, file downloads, phone clicks
- **Custom Event Recommendations**: Tailored to your business model

### 🛠️ **GTM Container Generation**
- **Ready-to-Import JSON**: Complete GTM container with tags, triggers, and variables
- **GA4 Setup**: Modern analytics implementation with Enhanced Ecommerce
- **Conversion Tracking**: Pre-configured events for identified opportunities
- **Data Layer Structure**: Recommended implementation with code examples

### 📋 **Professional Reports**
- **Executive Summary**: High-level findings with audit score
- **Technical Analysis**: Detailed technical findings and recommendations
- **Implementation Plan**: Step-by-step setup instructions
- **Testing Checklist**: QA guidelines for validation

## Quick Start

### Prerequisites
- Python 3.8+
- Chrome browser (for Selenium WebDriver)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/primeanalytics-ai-agent.git
cd primeanalytics-ai-agent
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Access the web interface**
Open your browser and go to `http://localhost:5000`

## Usage

### Web Interface
1. Enter the website URL you want to analyze
2. Click "Start Analytics Audit"
3. Wait for the analysis to complete (typically 30-60 seconds)
4. Review the comprehensive report
5. Download the GTM container JSON and audit report

### API Usage
```python
from website_analyzer import WebsiteAnalyzer
from gtm_generator import GTMGenerator
from report_generator import ReportGenerator

# Initialize analyzer
analyzer = WebsiteAnalyzer()

# Analyze website
result = analyzer.analyze('https://example.com')

# Generate GTM container
gtm_generator = GTMGenerator()
gtm_json = gtm_generator.generate_container(result)

# Generate report
report_generator = ReportGenerator()
report = report_generator.generate_report(result, gtm_json)
```

## Architecture

### Core Components

#### 🕷️ **WebsiteAnalyzer** (`website_analyzer.py`)
- **CMS Detection**: Uses pattern matching and technology fingerprinting
- **Analytics Detection**: Selenium-based JavaScript execution to detect tracking codes
- **Content Analysis**: Identifies forms, buttons, and conversion opportunities
- **Technical Audit**: Checks HTTPS, mobile optimization, schema markup

#### 🏗️ **GTMGenerator** (`gtm_generator.py`)
- **Container Structure**: Creates proper GTM export format
- **Dynamic Tag Generation**: Based on detected opportunities
- **Variable Creation**: Data layer variables for conversion tracking
- **Trigger Configuration**: Event-based and interaction triggers

#### 📊 **ReportGenerator** (`report_generator.py`)
- **Audit Scoring**: 100-point scoring system
- **Recommendations**: Prioritized action items
- **Implementation Guidance**: Step-by-step instructions
- **Code Examples**: Data layer and tracking code samples

### Supported Platforms

#### CMS Platforms
- WordPress
- Shopify / Shopify Plus
- Webflow
- Squarespace
- Wix
- Magento
- Drupal
- Joomla

#### Analytics & Tracking
- Google Tag Manager
- Google Analytics 4
- Universal Analytics
- Facebook Pixel
- TikTok Pixel
- Pinterest Tag
- LinkedIn Insight Tag
- Google Ads
- Hotjar
- Crazy Egg

#### Consent Management
- OneTrust
- Cookiebot
- CookieYes
- Klaro

## GTM Container Features

### Generated Tags
- **GA4 Configuration**: Main analytics setup
- **Page View Tracking**: Enhanced page view events
- **E-commerce Events**: view_item, add_to_cart, begin_checkout, purchase
- **Lead Generation**: Form submissions, sign-ups
- **Engagement Events**: File downloads, video interactions, phone clicks

### Included Triggers
- **Page Views**: All pages, specific pages
- **User Interactions**: Clicks, form submissions
- **Custom Events**: Business-specific conversion points
- **Enhanced E-commerce**: Shopping funnel triggers

### Pre-configured Variables
- **GA4 Configuration**: Centralized measurement ID
- **Data Layer Variables**: For conversion data
- **Built-in Variables**: Page URL, click elements, form data

## Conversion Tracking

### E-commerce
```javascript
// Enhanced E-commerce Purchase Event
dataLayer.push({
    'event': 'purchase',
    'ecommerce': {
        'transaction_id': '12345',
        'value': 25.42,
        'currency': 'USD',
        'items': [{
            'item_id': 'SKU123',
            'item_name': 'Product Name',
            'category': 'Category',
            'quantity': 1,
            'price': 25.42
        }]
    }
});
```

### Lead Generation
```javascript
// Lead Generation Event
dataLayer.push({
    'event': 'generate_lead',
    'form_name': 'Contact Form',
    'form_id': 'contact-form-1',
    'lead_type': 'contact_inquiry',
    'lead_source': 'website_form'
});
```

## Professional Use Cases

### For Marketing Agencies
- **Client Audits**: Quick comprehensive analytics audits
- **Onboarding**: Standardized GTM setup for new clients
- **Compliance**: GDPR/CCPA compliant tracking implementation
- **Reporting**: Professional audit reports for client presentations

### For E-commerce Brands
- **Revenue Tracking**: Complete purchase funnel analysis
- **Conversion Optimization**: Identify tracking gaps and opportunities
- **Cross-platform**: Shopify, WooCommerce, and custom stores
- **Performance**: Advanced e-commerce analytics setup

### For Consultants
- **Audit Services**: Professional website analytics audits
- **Implementation**: Ready-to-use GTM containers
- **Documentation**: Comprehensive setup and testing guides
- **Scalability**: Batch analysis for multiple clients

## Advanced Configuration

### Custom Event Tracking
Add custom conversion events by modifying the `_identify_conversion_opportunities` method in `website_analyzer.py`:

```python
# Add custom opportunity detection
if 'custom_indicator' in content:
    opportunities.append({
        'type': 'custom_conversion',
        'events': ['custom_event'],
        'priority': 'high',
        'description': 'Custom conversion tracking'
    })
```

### Environment Variables
Create a `.env` file for configuration:
```env
# Optional: OpenAI API key for enhanced analysis
OPENAI_API_KEY=your_openai_api_key

# Optional: Custom user agent
USER_AGENT=Your Custom User Agent

# Optional: Analysis timeout (seconds)
ANALYSIS_TIMEOUT=30
```

## Deployment

### Production Deployment
```bash
# Install production dependencies
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install Chrome for Selenium
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Code Style
- Follow PEP 8 guidelines
- Use type hints where possible
- Add docstrings for all functions
- Include error handling

## Support

### Troubleshooting

#### Chrome Driver Issues
If you encounter WebDriver issues:
```bash
# Update Chrome driver
pip install --upgrade webdriver-manager
```

#### Memory Issues
For large-scale analysis:
```python
# Increase timeout for heavy websites
analyzer = WebsiteAnalyzer()
analyzer.timeout = 60  # seconds
```

### Professional Services

For custom implementations, advanced integrations, or consulting services, contact PrimeAnalytics Solutions:

- **Website**: [Contact for custom solutions]
- **Email**: [Professional consultation available]
- **Services**: Custom analytics implementations, team training, enterprise solutions

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built for the digital analytics community
- Inspired by the need for automated, professional-grade analytics audits
- Designed to bridge the gap between technical implementation and business objectives

---

**PrimeAnalytics AI Agent** - Empowering businesses with data clarity through automated analytics auditing and implementation.