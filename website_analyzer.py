import requests
from bs4 import BeautifulSoup
import re
import json
from urllib.parse import urljoin, urlparse
import builtwith
import validators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class WebsiteAnalyzer:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def analyze(self, url):
        """Main analysis function that orchestrates all checks"""
        if not validators.url(url):
            raise ValueError("Invalid URL provided")
        
        # Ensure URL has protocol
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        print(f"Analyzing website: {url}")
        
        result = {
            'url': url,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'basic_info': {},
            'cms_detection': {},
            'analytics_detection': {},
            'tracking_analysis': {},
            'conversion_opportunities': {},
            'technical_analysis': {},
            'recommendations': []
        }
        
        try:
            # Basic website info
            result['basic_info'] = self._get_basic_info(url)
            
            # CMS Detection
            result['cms_detection'] = self._detect_cms(url)
            
            # Analytics Detection
            result['analytics_detection'] = self._detect_analytics(url)
            
            # Tracking Analysis
            result['tracking_analysis'] = self._analyze_tracking(url)
            
            # Conversion Opportunities
            result['conversion_opportunities'] = self._identify_conversion_opportunities(url)
            
            # Technical Analysis
            result['technical_analysis'] = self._technical_analysis(url)
            
            # Generate recommendations
            result['recommendations'] = self._generate_recommendations(result)
            
        except Exception as e:
            result['error'] = str(e)
            print(f"Error during analysis: {e}")
        
        return result
    
    def _get_basic_info(self, url):
        """Get basic website information"""
        try:
            response = self.session.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract meta information
            title = soup.find('title')
            title_text = title.text.strip() if title else "No title found"
            
            description_meta = soup.find('meta', attrs={'name': 'description'})
            description = description_meta.get('content', '') if description_meta else ''
            
            # Check for common meta tags
            og_title = soup.find('meta', attrs={'property': 'og:title'})
            og_description = soup.find('meta', attrs={'property': 'og:description'})
            
            return {
                'title': title_text,
                'description': description,
                'og_title': og_title.get('content', '') if og_title else '',
                'og_description': og_description.get('content', '') if og_description else '',
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds(),
                'content_length': len(response.content)
            }
        except Exception as e:
            return {'error': str(e)}
    
    def _detect_cms(self, url):
        """Detect CMS and technology stack"""
        try:
            # Use builtwith library for technology detection
            technologies = builtwith.parse(url)
            
            # Get page source for manual detection
            response = self.session.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            content = response.text.lower()
            
            cms_indicators = {
                'WordPress': [
                    '/wp-content/',
                    '/wp-includes/',
                    'wp-json',
                    'wordpress'
                ],
                'Shopify': [
                    'shopify',
                    'shopifycdn',
                    'myshopify.com',
                    'cdn.shopify.com'
                ],
                'Webflow': [
                    'webflow',
                    'wfcdn.com',
                    'webflow.io'
                ],
                'Squarespace': [
                    'squarespace',
                    'sqsp.com',
                    'squarespace-cdn'
                ],
                'Wix': [
                    'wix.com',
                    'wixstatic.com',
                    'wixsite.com'
                ],
                'Magento': [
                    'magento',
                    'mage',
                    '/skin/frontend/'
                ],
                'Drupal': [
                    'drupal',
                    '/sites/default/',
                    'drupal.js'
                ],
                'Joomla': [
                    'joomla',
                    '/templates/',
                    'joomla.js'
                ]
            }
            
            detected_cms = []
            confidence_scores = {}
            
            # Check for CMS indicators in content
            for cms, indicators in cms_indicators.items():
                matches = sum(1 for indicator in indicators if indicator in content)
                if matches > 0:
                    detected_cms.append(cms)
                    confidence_scores[cms] = matches / len(indicators)
            
            # Check meta generators
            generator_meta = soup.find('meta', attrs={'name': 'generator'})
            generator = generator_meta.get('content', '') if generator_meta else ''
            
            return {
                'technologies': technologies,
                'detected_cms': detected_cms,
                'confidence_scores': confidence_scores,
                'generator': generator,
                'primary_cms': max(confidence_scores.items(), key=lambda x: x[1])[0] if confidence_scores else 'Unknown'
            }
        except Exception as e:
            return {'error': str(e)}
    
    def _detect_analytics(self, url):
        """Detect analytics and tracking implementations"""
        try:
            # Get page source with JavaScript execution
            driver = self._get_driver()
            driver.get(url)
            time.sleep(3)  # Wait for scripts to load
            
            # Check for GTM
            gtm_containers = []
            gtm_scripts = driver.find_elements(By.XPATH, "//script[contains(text(), 'GTM-')]")
            for script in gtm_scripts:
                matches = re.findall(r'GTM-[A-Z0-9]+', script.get_attribute('innerHTML') or '')
                gtm_containers.extend(matches)
            
            # Check for GA4
            ga4_ids = []
            ga4_scripts = driver.find_elements(By.XPATH, "//script[contains(text(), 'G-')]")
            for script in ga4_scripts:
                matches = re.findall(r'G-[A-Z0-9]+', script.get_attribute('innerHTML') or '')
                ga4_ids.extend(matches)
            
            # Check for Universal Analytics
            ua_ids = []
            ua_scripts = driver.find_elements(By.XPATH, "//script[contains(text(), 'UA-')]")
            for script in ua_scripts:
                matches = re.findall(r'UA-\d+-\d+', script.get_attribute('innerHTML') or '')
                ua_ids.extend(matches)
            
            # Check for Facebook Pixel
            fb_pixels = []
            fb_scripts = driver.find_elements(By.XPATH, "//script[contains(text(), 'fbq')]")
            for script in fb_scripts:
                matches = re.findall(r'fbq\([\'"]init[\'"],\s*[\'"](\d+)[\'"]', script.get_attribute('innerHTML') or '')
                fb_pixels.extend(matches)
            
            # Check for other tracking
            other_tracking = {
                'hotjar': len(driver.find_elements(By.XPATH, "//script[contains(@src, 'hotjar')]")) > 0,
                'crazyegg': len(driver.find_elements(By.XPATH, "//script[contains(@src, 'crazyegg')]")) > 0,
                'linkedin': len(driver.find_elements(By.XPATH, "//script[contains(text(), '_linkedin_partner_id')]")) > 0,
                'tiktok': len(driver.find_elements(By.XPATH, "//script[contains(text(), 'ttq')]")) > 0,
                'pinterest': len(driver.find_elements(By.XPATH, "//script[contains(text(), 'pintrk')]")) > 0,
                'google_ads': len(driver.find_elements(By.XPATH, "//script[contains(@src, 'googleadservices')]")) > 0
            }
            
            # Check for consent management
            consent_tools = {
                'cookiebot': len(driver.find_elements(By.XPATH, "//script[contains(@src, 'cookiebot')]")) > 0,
                'onetrust': len(driver.find_elements(By.XPATH, "//script[contains(@src, 'onetrust')]")) > 0,
                'cookieyes': len(driver.find_elements(By.XPATH, "//script[contains(@src, 'cookieyes')]")) > 0,
                'klaro': len(driver.find_elements(By.XPATH, "//script[contains(text(), 'klaro')]")) > 0
            }
            
            driver.quit()
            
            return {
                'gtm_containers': list(set(gtm_containers)),
                'ga4_measurement_ids': list(set(ga4_ids)),
                'universal_analytics_ids': list(set(ua_ids)),
                'facebook_pixels': list(set(fb_pixels)),
                'other_tracking': other_tracking,
                'consent_management': consent_tools,
                'has_gtm': len(gtm_containers) > 0,
                'has_ga4': len(ga4_ids) > 0,
                'has_consent_management': any(consent_tools.values())
            }
        except Exception as e:
            return {'error': str(e)}
    
    def _analyze_tracking(self, url):
        """Analyze current tracking implementation"""
        try:
            response = self.session.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Check for forms
            forms = soup.find_all('form')
            form_analysis = []
            
            for i, form in enumerate(forms):
                form_info = {
                    'index': i,
                    'action': form.get('action', ''),
                    'method': form.get('method', 'GET'),
                    'inputs': [],
                    'has_tracking': False
                }
                
                # Analyze form inputs
                inputs = form.find_all(['input', 'textarea', 'select'])
                for inp in inputs:
                    input_info = {
                        'type': inp.get('type', inp.name),
                        'name': inp.get('name', ''),
                        'id': inp.get('id', ''),
                        'placeholder': inp.get('placeholder', '')
                    }
                    form_info['inputs'].append(input_info)
                
                # Check if form has tracking events
                onclick = form.get('onclick', '')
                onsubmit = form.get('onsubmit', '')
                if 'gtag' in onclick or 'gtag' in onsubmit or 'dataLayer' in onclick or 'dataLayer' in onsubmit:
                    form_info['has_tracking'] = True
                
                form_analysis.append(form_info)
            
            # Check for buttons with tracking
            buttons = soup.find_all(['button', 'a'])
            button_analysis = []
            
            for button in buttons:
                if button.get('onclick') or button.get('href'):
                    onclick = button.get('onclick', '')
                    href = button.get('href', '')
                    text = button.get_text(strip=True)
                    
                    if 'gtag' in onclick or 'dataLayer' in onclick or any(keyword in text.lower() for keyword in ['buy', 'purchase', 'add to cart', 'subscribe', 'contact', 'download']):
                        button_analysis.append({
                            'text': text,
                            'href': href,
                            'onclick': onclick,
                            'has_tracking': 'gtag' in onclick or 'dataLayer' in onclick
                        })
            
            return {
                'forms_count': len(forms),
                'forms_analysis': form_analysis,
                'tracked_buttons': button_analysis,
                'forms_with_tracking': sum(1 for form in form_analysis if form['has_tracking'])
            }
        except Exception as e:
            return {'error': str(e)}
    
    def _identify_conversion_opportunities(self, url):
        """Identify potential conversion events that should be tracked"""
        try:
            response = self.session.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            content = response.text.lower()
            
            opportunities = []
            
            # E-commerce indicators
            ecommerce_indicators = [
                'add to cart', 'buy now', 'purchase', 'checkout', 'shop now',
                'add to bag', 'add to basket', 'price', '$', '€', '£'
            ]
            
            if any(indicator in content for indicator in ecommerce_indicators):
                opportunities.append({
                    'type': 'ecommerce',
                    'events': ['view_item', 'add_to_cart', 'begin_checkout', 'purchase'],
                    'priority': 'high',
                    'description': 'E-commerce tracking for product interactions and purchases'
                })
            
            # Lead generation indicators
            lead_gen_indicators = [
                'contact', 'get quote', 'request demo', 'sign up', 'subscribe',
                'newsletter', 'download', 'whitepaper', 'ebook'
            ]
            
            if any(indicator in content for indicator in lead_gen_indicators):
                opportunities.append({
                    'type': 'lead_generation',
                    'events': ['generate_lead', 'sign_up', 'subscribe'],
                    'priority': 'high',
                    'description': 'Lead generation tracking for form submissions and sign-ups'
                })
            
            # Engagement indicators
            if soup.find_all('video') or 'youtube' in content or 'vimeo' in content:
                opportunities.append({
                    'type': 'engagement',
                    'events': ['video_start', 'video_progress', 'video_complete'],
                    'priority': 'medium',
                    'description': 'Video engagement tracking'
                })
            
            # File download indicators
            download_links = soup.find_all('a', href=re.compile(r'\.(pdf|doc|docx|xls|xlsx|zip|mp4|mp3)$', re.I))
            if download_links:
                opportunities.append({
                    'type': 'file_download',
                    'events': ['file_download'],
                    'priority': 'medium',
                    'description': 'File download tracking for PDFs, documents, and media files'
                })
            
            # Phone number tracking
            phone_pattern = r'(\+\d{1,3}[-.\s]?)?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}'
            if re.search(phone_pattern, content):
                opportunities.append({
                    'type': 'phone_tracking',
                    'events': ['phone_click'],
                    'priority': 'medium',
                    'description': 'Phone number click tracking'
                })
            
            return {
                'total_opportunities': len(opportunities),
                'opportunities': opportunities,
                'recommended_events': list(set([event for opp in opportunities for event in opp['events']]))
            }
        except Exception as e:
            return {'error': str(e)}
    
    def _technical_analysis(self, url):
        """Perform technical analysis of the website"""
        try:
            response = self.session.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Check for data layer
            has_data_layer = 'datalayer' in response.text.lower() or 'data-layer' in response.text.lower()
            
            # Check for schema markup
            schema_scripts = soup.find_all('script', type='application/ld+json')
            has_schema = len(schema_scripts) > 0
            
            # Check for AMP
            has_amp = soup.find('html', {'amp': True}) is not None or soup.find('html', {'⚡': True}) is not None
            
            # Check for service worker
            has_service_worker = 'serviceworker' in response.text.lower()
            
            # Check for HTTPS
            is_https = url.startswith('https://')
            
            # Check for mobile optimization
            viewport_meta = soup.find('meta', attrs={'name': 'viewport'})
            is_mobile_optimized = viewport_meta is not None
            
            return {
                'has_data_layer': has_data_layer,
                'has_schema_markup': has_schema,
                'schema_count': len(schema_scripts),
                'has_amp': has_amp,
                'has_service_worker': has_service_worker,
                'is_https': is_https,
                'is_mobile_optimized': is_mobile_optimized,
                'page_load_time': response.elapsed.total_seconds()
            }
        except Exception as e:
            return {'error': str(e)}
    
    def _generate_recommendations(self, analysis_result):
        """Generate actionable recommendations based on analysis"""
        recommendations = []
        
        # Analytics recommendations
        analytics = analysis_result.get('analytics_detection', {})
        
        if not analytics.get('has_gtm'):
            recommendations.append({
                'category': 'Analytics Setup',
                'priority': 'High',
                'title': 'Implement Google Tag Manager',
                'description': 'GTM is not detected. Implementing GTM will provide better tag management and tracking flexibility.',
                'action': 'Install GTM container'
            })
        
        if not analytics.get('has_ga4'):
            recommendations.append({
                'category': 'Analytics Setup',
                'priority': 'High',
                'title': 'Implement Google Analytics 4',
                'description': 'GA4 is not detected. GA4 is essential for modern analytics and will be the only version of Google Analytics available.',
                'action': 'Install GA4 measurement'
            })
        
        if not analytics.get('has_consent_management'):
            recommendations.append({
                'category': 'Privacy Compliance',
                'priority': 'High',
                'title': 'Implement Consent Management',
                'description': 'No consent management platform detected. This is crucial for GDPR/CCPA compliance.',
                'action': 'Install consent management platform'
            })
        
        # Conversion tracking recommendations
        conversion_opps = analysis_result.get('conversion_opportunities', {})
        if conversion_opps.get('total_opportunities', 0) > 0:
            recommendations.append({
                'category': 'Conversion Tracking',
                'priority': 'High',
                'title': 'Implement Conversion Events',
                'description': f'Found {conversion_opps.get("total_opportunities")} conversion opportunities that should be tracked.',
                'action': 'Set up conversion event tracking'
            })
        
        # Technical recommendations
        technical = analysis_result.get('technical_analysis', {})
        
        if not technical.get('has_data_layer'):
            recommendations.append({
                'category': 'Technical Setup',
                'priority': 'Medium',
                'title': 'Implement Data Layer',
                'description': 'Data layer not detected. A proper data layer structure will improve tracking accuracy and flexibility.',
                'action': 'Implement structured data layer'
            })
        
        if not technical.get('is_https'):
            recommendations.append({
                'category': 'Security',
                'priority': 'High',
                'title': 'Enable HTTPS',
                'description': 'Website is not using HTTPS. This affects tracking accuracy and user trust.',
                'action': 'Implement SSL certificate'
            })
        
        return recommendations
    
    def _get_driver(self):
        """Get Selenium WebDriver with appropriate options"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        
        try:
            driver = webdriver.Chrome(options=chrome_options)
            return driver
        except Exception as e:
            print(f"Error creating WebDriver: {e}")
            raise