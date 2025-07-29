import json
from datetime import datetime

class ReportGenerator:
    def __init__(self):
        self.report_version = "1.0"
    
    def generate_report(self, analysis_result, gtm_json):
        """Generate a comprehensive audit report"""
        
        report = {
            "report_metadata": {
                "generated_at": datetime.now().isoformat(),
                "report_version": self.report_version,
                "website_url": analysis_result.get('url', ''),
                "analysis_timestamp": analysis_result.get('timestamp', '')
            },
            "executive_summary": self._generate_executive_summary(analysis_result),
            "technical_findings": self._generate_technical_findings(analysis_result),
            "analytics_audit": self._generate_analytics_audit(analysis_result),
            "conversion_opportunities": self._format_conversion_opportunities(analysis_result),
            "implementation_plan": self._generate_implementation_plan(analysis_result, gtm_json),
            "recommendations": self._format_recommendations(analysis_result),
            "next_steps": self._generate_next_steps(analysis_result)
        }
        
        return report
    
    def _generate_executive_summary(self, analysis_result):
        """Generate executive summary of findings"""
        
        basic_info = analysis_result.get('basic_info', {})
        cms = analysis_result.get('cms_detection', {}).get('primary_cms', 'Unknown')
        analytics = analysis_result.get('analytics_detection', {})
        opportunities = analysis_result.get('conversion_opportunities', {})
        recommendations = analysis_result.get('recommendations', [])
        
        # Calculate audit score
        audit_score = self._calculate_audit_score(analysis_result)
        
        summary = {
            "website_title": basic_info.get('title', 'Not found'),
            "cms_platform": cms,
            "audit_score": audit_score,
            "critical_issues": len([r for r in recommendations if r.get('priority') == 'High']),
            "optimization_opportunities": opportunities.get('total_opportunities', 0),
            "current_analytics_setup": {
                "has_gtm": analytics.get('has_gtm', False),
                "has_ga4": analytics.get('has_ga4', False),
                "has_consent_management": analytics.get('has_consent_management', False)
            },
            "key_findings": self._extract_key_findings(analysis_result)
        }
        
        return summary
    
    def _generate_technical_findings(self, analysis_result):
        """Generate detailed technical findings"""
        
        basic_info = analysis_result.get('basic_info', {})
        cms_detection = analysis_result.get('cms_detection', {})
        technical = analysis_result.get('technical_analysis', {})
        
        findings = {
            "website_performance": {
                "page_load_time": technical.get('page_load_time', 0),
                "response_time": basic_info.get('response_time', 0),
                "content_length": basic_info.get('content_length', 0),
                "status_code": basic_info.get('status_code', 0)
            },
            "cms_and_technology": {
                "detected_cms": cms_detection.get('detected_cms', []),
                "confidence_scores": cms_detection.get('confidence_scores', {}),
                "technologies": cms_detection.get('technologies', {}),
                "generator": cms_detection.get('generator', '')
            },
            "technical_setup": {
                "is_https": technical.get('is_https', False),
                "has_data_layer": technical.get('has_data_layer', False),
                "has_schema_markup": technical.get('has_schema_markup', False),
                "schema_count": technical.get('schema_count', 0),
                "is_mobile_optimized": technical.get('is_mobile_optimized', False),
                "has_amp": technical.get('has_amp', False),
                "has_service_worker": technical.get('has_service_worker', False)
            }
        }
        
        return findings
    
    def _generate_analytics_audit(self, analysis_result):
        """Generate analytics audit section"""
        
        analytics = analysis_result.get('analytics_detection', {})
        tracking = analysis_result.get('tracking_analysis', {})
        
        audit = {
            "current_implementation": {
                "google_tag_manager": {
                    "installed": analytics.get('has_gtm', False),
                    "containers": analytics.get('gtm_containers', []),
                    "container_count": len(analytics.get('gtm_containers', []))
                },
                "google_analytics": {
                    "ga4_installed": analytics.get('has_ga4', False),
                    "ga4_measurement_ids": analytics.get('ga4_measurement_ids', []),
                    "universal_analytics_ids": analytics.get('universal_analytics_ids', []),
                    "using_legacy_ua": len(analytics.get('universal_analytics_ids', [])) > 0
                },
                "other_tracking": analytics.get('other_tracking', {}),
                "facebook_pixel": {
                    "installed": len(analytics.get('facebook_pixels', [])) > 0,
                    "pixel_ids": analytics.get('facebook_pixels', [])
                }
            },
            "privacy_compliance": {
                "consent_management": analytics.get('consent_management', {}),
                "has_consent_solution": analytics.get('has_consent_management', False)
            },
            "tracking_assessment": {
                "total_forms": tracking.get('forms_count', 0),
                "forms_with_tracking": tracking.get('forms_with_tracking', 0),
                "tracked_buttons": len(tracking.get('tracked_buttons', [])),
                "form_analysis": tracking.get('forms_analysis', [])
            }
        }
        
        return audit
    
    def _format_conversion_opportunities(self, analysis_result):
        """Format conversion opportunities for the report"""
        
        opportunities = analysis_result.get('conversion_opportunities', {})
        
        formatted_opportunities = {
            "summary": {
                "total_opportunities": opportunities.get('total_opportunities', 0),
                "recommended_events": opportunities.get('recommended_events', [])
            },
            "detailed_opportunities": []
        }
        
        for opp in opportunities.get('opportunities', []):
            formatted_opp = {
                "type": opp.get('type', ''),
                "priority": opp.get('priority', ''),
                "description": opp.get('description', ''),
                "recommended_events": opp.get('events', []),
                "implementation_notes": self._get_implementation_notes(opp.get('type', ''))
            }
            formatted_opportunities["detailed_opportunities"].append(formatted_opp)
        
        return formatted_opportunities
    
    def _generate_implementation_plan(self, analysis_result, gtm_json):
        """Generate implementation plan based on GTM JSON"""
        
        plan = {
            "gtm_setup": {
                "container_structure": {
                    "tags_count": len(gtm_json.get('containerVersion', {}).get('tag', [])),
                    "triggers_count": len(gtm_json.get('containerVersion', {}).get('trigger', [])),
                    "variables_count": len(gtm_json.get('containerVersion', {}).get('variable', []))
                },
                "implementation_steps": [
                    {
                        "step": 1,
                        "title": "Create GTM Container",
                        "description": "Create a new GTM container or use existing one",
                        "estimated_time": "5 minutes"
                    },
                    {
                        "step": 2,
                        "title": "Import Container JSON",
                        "description": "Import the generated GTM container JSON file",
                        "estimated_time": "2 minutes"
                    },
                    {
                        "step": 3,
                        "title": "Update Configuration Variables",
                        "description": "Update GA4 Configuration variable with actual Measurement ID",
                        "estimated_time": "3 minutes"
                    },
                    {
                        "step": 4,
                        "title": "Install GTM Code",
                        "description": "Add GTM code to website header and body",
                        "estimated_time": "10 minutes"
                    },
                    {
                        "step": 5,
                        "title": "Implement Data Layer",
                        "description": "Add data layer structure to website pages",
                        "estimated_time": "30-60 minutes"
                    },
                    {
                        "step": 6,
                        "title": "Test Implementation",
                        "description": "Test all tags and triggers using GTM Preview mode",
                        "estimated_time": "20 minutes"
                    },
                    {
                        "step": 7,
                        "title": "Publish Container",
                        "description": "Publish the GTM container to production",
                        "estimated_time": "2 minutes"
                    }
                ]
            },
            "data_layer_structure": self._generate_data_layer_structure(analysis_result),
            "testing_checklist": self._generate_testing_checklist(analysis_result)
        }
        
        return plan
    
    def _format_recommendations(self, analysis_result):
        """Format recommendations for the report"""
        
        recommendations = analysis_result.get('recommendations', [])
        
        formatted_recs = {
            "high_priority": [r for r in recommendations if r.get('priority') == 'High'],
            "medium_priority": [r for r in recommendations if r.get('priority') == 'Medium'],
            "low_priority": [r for r in recommendations if r.get('priority') == 'Low']
        }
        
        return formatted_recs
    
    def _generate_next_steps(self, analysis_result):
        """Generate next steps and action items"""
        
        analytics = analysis_result.get('analytics_detection', {})
        opportunities = analysis_result.get('conversion_opportunities', {})
        
        next_steps = {
            "immediate_actions": [],
            "week_1_goals": [],
            "month_1_goals": [],
            "ongoing_optimization": []
        }
        
        # Immediate actions
        if not analytics.get('has_gtm'):
            next_steps["immediate_actions"].append({
                "action": "Install Google Tag Manager",
                "priority": "Critical",
                "estimated_effort": "1-2 hours"
            })
        
        if not analytics.get('has_ga4'):
            next_steps["immediate_actions"].append({
                "action": "Set up Google Analytics 4",
                "priority": "Critical",
                "estimated_effort": "30 minutes"
            })
        
        # Week 1 goals
        if opportunities.get('total_opportunities', 0) > 0:
            next_steps["week_1_goals"].append({
                "goal": "Implement conversion tracking for identified opportunities",
                "deliverable": "All conversion events tracked in GA4"
            })
        
        next_steps["week_1_goals"].append({
            "goal": "Test and validate all tracking implementation",
            "deliverable": "QA report confirming accurate data collection"
        })
        
        # Month 1 goals
        next_steps["month_1_goals"].append({
            "goal": "Set up automated reporting dashboard",
            "deliverable": "Looker Studio dashboard with key metrics"
        })
        
        if not analytics.get('has_consent_management'):
            next_steps["month_1_goals"].append({
                "goal": "Implement privacy compliance solution",
                "deliverable": "GDPR/CCPA compliant consent management"
            })
        
        # Ongoing optimization
        next_steps["ongoing_optimization"] = [
            {
                "activity": "Monthly analytics audit and optimization",
                "frequency": "Monthly"
            },
            {
                "activity": "Conversion rate optimization based on data insights",
                "frequency": "Quarterly"
            },
            {
                "activity": "Enhanced ecommerce tracking refinement",
                "frequency": "As needed"
            }
        ]
        
        return next_steps
    
    def _calculate_audit_score(self, analysis_result):
        """Calculate overall audit score (0-100)"""
        
        score = 0
        max_score = 100
        
        analytics = analysis_result.get('analytics_detection', {})
        technical = analysis_result.get('technical_analysis', {})
        opportunities = analysis_result.get('conversion_opportunities', {})
        
        # Analytics setup (40 points)
        if analytics.get('has_gtm'):
            score += 15
        if analytics.get('has_ga4'):
            score += 15
        if analytics.get('has_consent_management'):
            score += 10
        
        # Technical setup (30 points)
        if technical.get('is_https'):
            score += 10
        if technical.get('has_data_layer'):
            score += 10
        if technical.get('is_mobile_optimized'):
            score += 5
        if technical.get('has_schema_markup'):
            score += 5
        
        # Conversion tracking (30 points)
        total_opps = opportunities.get('total_opportunities', 0)
        if total_opps == 0:
            score += 30  # No opportunities found, perfect score
        else:
            # Score based on implementation readiness
            tracking = analysis_result.get('tracking_analysis', {})
            forms_with_tracking = tracking.get('forms_with_tracking', 0)
            total_forms = tracking.get('forms_count', 1)
            
            tracking_ratio = forms_with_tracking / max(total_forms, 1)
            score += int(30 * tracking_ratio)
        
        return min(score, max_score)
    
    def _extract_key_findings(self, analysis_result):
        """Extract key findings for executive summary"""
        
        findings = []
        
        analytics = analysis_result.get('analytics_detection', {})
        technical = analysis_result.get('technical_analysis', {})
        opportunities = analysis_result.get('conversion_opportunities', {})
        cms = analysis_result.get('cms_detection', {}).get('primary_cms', 'Unknown')
        
        # CMS finding
        if cms != 'Unknown':
            findings.append(f"Website built on {cms} platform")
        
        # Analytics findings
        if not analytics.get('has_gtm'):
            findings.append("Google Tag Manager not implemented")
        
        if not analytics.get('has_ga4'):
            findings.append("Google Analytics 4 not detected")
        
        # Conversion opportunities
        total_opps = opportunities.get('total_opportunities', 0)
        if total_opps > 0:
            findings.append(f"{total_opps} conversion tracking opportunities identified")
        
        # Privacy compliance
        if not analytics.get('has_consent_management'):
            findings.append("No consent management solution detected")
        
        # Technical issues
        if not technical.get('is_https'):
            findings.append("Website not using HTTPS")
        
        return findings[:5]  # Return top 5 findings
    
    def _get_implementation_notes(self, opportunity_type):
        """Get implementation notes for different opportunity types"""
        
        notes = {
            'ecommerce': [
                "Implement Enhanced Ecommerce data layer structure",
                "Track all funnel steps: view_item, add_to_cart, begin_checkout, purchase",
                "Include product details in event parameters",
                "Set up revenue and conversion value tracking"
            ],
            'lead_generation': [
                "Track form submissions with form identification",
                "Implement lead scoring if applicable",
                "Set up goal values for different lead types",
                "Track multi-step forms completion"
            ],
            'engagement': [
                "Track video engagement milestones (25%, 50%, 75%, 100%)",
                "Monitor scroll depth for content engagement",
                "Track time on page for key content",
                "Implement custom engagement events"
            ],
            'file_download': [
                "Track all document downloads",
                "Categorize downloads by type",
                "Monitor popular downloads",
                "Set up conversion values for key downloads"
            ],
            'phone_tracking': [
                "Track phone number clicks",
                "Implement call tracking if budget allows",
                "Monitor mobile vs desktop phone interactions",
                "Set up phone call conversions"
            ]
        }
        
        return notes.get(opportunity_type, [])
    
    def _generate_data_layer_structure(self, analysis_result):
        """Generate recommended data layer structure"""
        
        opportunities = analysis_result.get('conversion_opportunities', {}).get('opportunities', [])
        
        structure = {
            "base_structure": {
                "description": "Basic data layer structure for all pages",
                "code": """
window.dataLayer = window.dataLayer || [];
dataLayer.push({
    'event': 'page_view',
    'page_title': document.title,
    'page_location': window.location.href,
    'page_path': window.location.pathname
});
                """.strip()
            },
            "event_specific": []
        }
        
        for opp in opportunities:
            if opp['type'] == 'ecommerce':
                structure["event_specific"].append({
                    "event_type": "E-commerce Events",
                    "description": "Data layer structure for e-commerce tracking",
                    "code": """
// Purchase Event
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

// Add to Cart Event
dataLayer.push({
    'event': 'add_to_cart',
    'ecommerce': {
        'currency': 'USD',
        'value': 25.42,
        'items': [{
            'item_id': 'SKU123',
            'item_name': 'Product Name',
            'category': 'Category',
            'quantity': 1,
            'price': 25.42
        }]
    }
});
                    """.strip()
                })
            
            elif opp['type'] == 'lead_generation':
                structure["event_specific"].append({
                    "event_type": "Lead Generation Events",
                    "description": "Data layer structure for lead tracking",
                    "code": """
// Form Submit Event
dataLayer.push({
    'event': 'generate_lead',
    'form_name': 'Contact Form',
    'form_id': 'contact-form-1',
    'lead_type': 'contact_inquiry',
    'lead_source': 'website_form'
});
                    """.strip()
                })
        
        return structure
    
    def _generate_testing_checklist(self, analysis_result):
        """Generate testing checklist for implementation"""
        
        opportunities = analysis_result.get('conversion_opportunities', {}).get('opportunities', [])
        
        checklist = {
            "basic_setup": [
                "GTM container loads on all pages",
                "GA4 Configuration tag fires on page load",
                "Page view events are tracked in GA4",
                "Real-time reports show data in GA4"
            ],
            "conversion_tracking": [],
            "privacy_compliance": [
                "Consent banner appears on first visit",
                "Tags respect user consent choices",
                "Consent Mode v2 is properly configured"
            ],
            "technical_validation": [
                "No JavaScript errors in console",
                "All GTM tags fire correctly in Preview mode",
                "Data layer pushes are working",
                "Cross-domain tracking configured if needed"
            ]
        }
        
        # Add conversion-specific testing items
        for opp in opportunities:
            if opp['type'] == 'ecommerce':
                checklist["conversion_tracking"].extend([
                    "Purchase events tracked with correct revenue",
                    "Add to cart events fire on button clicks",
                    "Product data is captured correctly",
                    "Enhanced ecommerce events appear in GA4"
                ])
            elif opp['type'] == 'lead_generation':
                checklist["conversion_tracking"].extend([
                    "Form submission events tracked",
                    "Lead data captured in GA4 events",
                    "Goal conversions configured in GA4"
                ])
        
        return checklist