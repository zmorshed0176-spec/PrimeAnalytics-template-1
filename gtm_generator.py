import json
import time
from datetime import datetime

class GTMGenerator:
    def __init__(self):
        self.container_version = "1"
        self.fingerprint = str(int(time.time() * 1000))
        
    def generate_container(self, analysis_result):
        """Generate a complete GTM container JSON based on website analysis"""
        
        # Extract information from analysis
        cms = analysis_result.get('cms_detection', {}).get('primary_cms', 'Unknown')
        opportunities = analysis_result.get('conversion_opportunities', {}).get('opportunities', [])
        analytics = analysis_result.get('analytics_detection', {})
        
        # Base container structure
        container = {
            "exportFormatVersion": 2,
            "exportTime": datetime.now().isoformat() + "Z",
            "containerVersion": {
                "path": f"accounts/YOUR_ACCOUNT_ID/containers/YOUR_CONTAINER_ID/versions/{self.container_version}",
                "accountId": "YOUR_ACCOUNT_ID",
                "containerId": "YOUR_CONTAINER_ID",
                "containerVersionId": self.container_version,
                "name": f"Analytics Setup - {cms} Website",
                "description": f"Auto-generated GTM setup for {cms} website with conversion tracking",
                "container": {
                    "path": "accounts/YOUR_ACCOUNT_ID/containers/YOUR_CONTAINER_ID",
                    "accountId": "YOUR_ACCOUNT_ID",
                    "containerId": "YOUR_CONTAINER_ID",
                    "name": "Auto-Generated Container",
                    "publicId": "GTM-XXXXXXX",
                    "usageContext": ["WEB"],
                    "fingerprint": self.fingerprint,
                    "tagManagerUrl": "https://tagmanager.google.com/#/container/accounts/YOUR_ACCOUNT_ID/containers/YOUR_CONTAINER_ID/workspaces?apiLink=container"
                },
                "tag": [],
                "trigger": [],
                "variable": [],
                "builtInVariable": self._get_builtin_variables()
            }
        }
        
        # Generate variables
        variables = self._generate_variables(analysis_result)
        container["containerVersion"]["variable"] = variables
        
        # Generate triggers
        triggers = self._generate_triggers(analysis_result)
        container["containerVersion"]["trigger"] = triggers
        
        # Generate tags
        tags = self._generate_tags(analysis_result, triggers, variables)
        container["containerVersion"]["tag"] = tags
        
        return container
    
    def _get_builtin_variables(self):
        """Get essential built-in variables"""
        return [
            {"accountId": "YOUR_ACCOUNT_ID", "containerId": "YOUR_CONTAINER_ID", "type": "PAGE_URL", "name": "Page URL"},
            {"accountId": "YOUR_ACCOUNT_ID", "containerId": "YOUR_CONTAINER_ID", "type": "PAGE_HOSTNAME", "name": "Page Hostname"},
            {"accountId": "YOUR_ACCOUNT_ID", "containerId": "YOUR_CONTAINER_ID", "type": "PAGE_PATH", "name": "Page Path"},
            {"accountId": "YOUR_ACCOUNT_ID", "containerId": "YOUR_CONTAINER_ID", "type": "REFERRER", "name": "Referrer"},
            {"accountId": "YOUR_ACCOUNT_ID", "containerId": "YOUR_CONTAINER_ID", "type": "EVENT", "name": "Event"},
            {"accountId": "YOUR_ACCOUNT_ID", "containerId": "YOUR_CONTAINER_ID", "type": "CLICK_ELEMENT", "name": "Click Element"},
            {"accountId": "YOUR_ACCOUNT_ID", "containerId": "YOUR_CONTAINER_ID", "type": "CLICK_TEXT", "name": "Click Text"},
            {"accountId": "YOUR_ACCOUNT_ID", "containerId": "YOUR_CONTAINER_ID", "type": "CLICK_URL", "name": "Click URL"},
            {"accountId": "YOUR_ACCOUNT_ID", "containerId": "YOUR_CONTAINER_ID", "type": "FORM_ELEMENT", "name": "Form Element"},
            {"accountId": "YOUR_ACCOUNT_ID", "containerId": "YOUR_CONTAINER_ID", "type": "FORM_TEXT", "name": "Form Text"}
        ]
    
    def _generate_variables(self, analysis_result):
        """Generate custom variables based on website analysis"""
        variables = []
        
        # GA4 Configuration Variable
        variables.append({
            "accountId": "YOUR_ACCOUNT_ID",
            "containerId": "YOUR_CONTAINER_ID",
            "variableId": "1",
            "name": "GA4 Configuration",
            "type": "gcs",
            "parameter": [
                {"type": "TEMPLATE", "key": "configId", "value": "G-XXXXXXXXXX"},
                {"type": "BOOLEAN", "key": "anonymizeIp", "value": "false"},
                {"type": "BOOLEAN", "key": "enableLinkDomains", "value": "false"},
                {"type": "MAP", "key": "customParameters", "map": [
                    {"type": "TEMPLATE", "key": "currency", "value": "USD"},
                    {"type": "TEMPLATE", "key": "send_page_view", "value": "true"}
                ]}
            ]
        })
        
        # Data Layer Variables based on opportunities
        opportunities = analysis_result.get('conversion_opportunities', {}).get('opportunities', [])
        
        if any(opp['type'] == 'ecommerce' for opp in opportunities):
            # E-commerce variables
            ecommerce_vars = [
                {"name": "DLV - Event Category", "dataLayerName": "event_category"},
                {"name": "DLV - Event Action", "dataLayerName": "event_action"},
                {"name": "DLV - Event Label", "dataLayerName": "event_label"},
                {"name": "DLV - Value", "dataLayerName": "value"},
                {"name": "DLV - Currency", "dataLayerName": "currency"},
                {"name": "DLV - Item ID", "dataLayerName": "item_id"},
                {"name": "DLV - Item Name", "dataLayerName": "item_name"},
                {"name": "DLV - Item Category", "dataLayerName": "item_category"},
                {"name": "DLV - Quantity", "dataLayerName": "quantity"},
                {"name": "DLV - Price", "dataLayerName": "price"}
            ]
            
            for i, var in enumerate(ecommerce_vars, start=2):
                variables.append({
                    "accountId": "YOUR_ACCOUNT_ID",
                    "containerId": "YOUR_CONTAINER_ID",
                    "variableId": str(i),
                    "name": var["name"],
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": var["dataLayerName"]}
                    ]
                })
        
        if any(opp['type'] == 'lead_generation' for opp in opportunities):
            # Lead generation variables
            lead_vars = [
                {"name": "DLV - Form Name", "dataLayerName": "form_name"},
                {"name": "DLV - Form ID", "dataLayerName": "form_id"},
                {"name": "DLV - Lead Type", "dataLayerName": "lead_type"},
                {"name": "DLV - Lead Source", "dataLayerName": "lead_source"}
            ]
            
            start_id = len(variables) + 1
            for i, var in enumerate(lead_vars, start=start_id):
                variables.append({
                    "accountId": "YOUR_ACCOUNT_ID",
                    "containerId": "YOUR_CONTAINER_ID",
                    "variableId": str(i),
                    "name": var["name"],
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": var["dataLayerName"]}
                    ]
                })
        
        return variables
    
    def _generate_triggers(self, analysis_result):
        """Generate triggers based on website analysis"""
        triggers = []
        
        # Page View trigger
        triggers.append({
            "accountId": "YOUR_ACCOUNT_ID",
            "containerId": "YOUR_CONTAINER_ID",
            "triggerId": "1",
            "name": "All Pages",
            "type": "PAGEVIEW"
        })
        
        # DOM Ready trigger
        triggers.append({
            "accountId": "YOUR_ACCOUNT_ID",
            "containerId": "YOUR_CONTAINER_ID",
            "triggerId": "2",
            "name": "DOM Ready",
            "type": "DOM_READY"
        })
        
        # Window Loaded trigger
        triggers.append({
            "accountId": "YOUR_ACCOUNT_ID",
            "containerId": "YOUR_CONTAINER_ID",
            "triggerId": "3",
            "name": "Window Loaded",
            "type": "WINDOW_LOADED"
        })
        
        opportunities = analysis_result.get('conversion_opportunities', {}).get('opportunities', [])
        trigger_id = 4
        
        # E-commerce triggers
        if any(opp['type'] == 'ecommerce' for opp in opportunities):
            ecommerce_triggers = [
                {"name": "View Item", "event": "view_item"},
                {"name": "Add to Cart", "event": "add_to_cart"},
                {"name": "Begin Checkout", "event": "begin_checkout"},
                {"name": "Purchase", "event": "purchase"}
            ]
            
            for trigger in ecommerce_triggers:
                triggers.append({
                    "accountId": "YOUR_ACCOUNT_ID",
                    "containerId": "YOUR_CONTAINER_ID",
                    "triggerId": str(trigger_id),
                    "name": trigger["name"],
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{Event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": trigger["event"]}
                            ]
                        }
                    ]
                })
                trigger_id += 1
        
        # Lead generation triggers
        if any(opp['type'] == 'lead_generation' for opp in opportunities):
            lead_triggers = [
                {"name": "Form Submit - All", "type": "FORM_SUBMISSION"},
                {"name": "Lead Generated", "event": "generate_lead"},
                {"name": "Newsletter Signup", "event": "sign_up"}
            ]
            
            for trigger in lead_triggers:
                if trigger.get("event"):
                    triggers.append({
                        "accountId": "YOUR_ACCOUNT_ID",
                        "containerId": "YOUR_CONTAINER_ID",
                        "triggerId": str(trigger_id),
                        "name": trigger["name"],
                        "type": "CUSTOM_EVENT",
                        "customEventFilter": [
                            {
                                "type": "EQUALS",
                                "parameter": [
                                    {"type": "TEMPLATE", "key": "arg0", "value": "{{Event}}"},
                                    {"type": "TEMPLATE", "key": "arg1", "value": trigger["event"]}
                                ]
                            }
                        ]
                    })
                else:
                    triggers.append({
                        "accountId": "YOUR_ACCOUNT_ID",
                        "containerId": "YOUR_CONTAINER_ID",
                        "triggerId": str(trigger_id),
                        "name": trigger["name"],
                        "type": trigger["type"],
                        "waitForTags": {
                            "value": "true",
                            "type": "BOOLEAN"
                        },
                        "checkValidation": {
                            "value": "true",
                            "type": "BOOLEAN"
                        }
                    })
                trigger_id += 1
        
        # File download triggers
        if any(opp['type'] == 'file_download' for opp in opportunities):
            triggers.append({
                "accountId": "YOUR_ACCOUNT_ID",
                "containerId": "YOUR_CONTAINER_ID",
                "triggerId": str(trigger_id),
                "name": "File Download",
                "type": "LINK_CLICK",
                "filter": [
                    {
                        "type": "MATCHES_REGEX",
                        "parameter": [
                            {"type": "TEMPLATE", "key": "arg0", "value": "{{Click URL}}"},
                            {"type": "TEMPLATE", "key": "arg1", "value": "\\.(pdf|doc|docx|xls|xlsx|zip|mp4|mp3)$"}
                        ]
                    }
                ],
                "waitForTags": {
                    "value": "true",
                    "type": "BOOLEAN"
                }
            })
            trigger_id += 1
        
        # Phone click triggers
        if any(opp['type'] == 'phone_tracking' for opp in opportunities):
            triggers.append({
                "accountId": "YOUR_ACCOUNT_ID",
                "containerId": "YOUR_CONTAINER_ID",
                "triggerId": str(trigger_id),
                "name": "Phone Click",
                "type": "LINK_CLICK",
                "filter": [
                    {
                        "type": "STARTS_WITH",
                        "parameter": [
                            {"type": "TEMPLATE", "key": "arg0", "value": "{{Click URL}}"},
                            {"type": "TEMPLATE", "key": "arg1", "value": "tel:"}
                        ]
                    }
                ],
                "waitForTags": {
                    "value": "true",
                    "type": "BOOLEAN"
                }
            })
            trigger_id += 1
        
        return triggers
    
    def _generate_tags(self, analysis_result, triggers, variables):
        """Generate tags based on analysis and triggers"""
        tags = []
        
        # GA4 Configuration tag
        tags.append({
            "accountId": "YOUR_ACCOUNT_ID",
            "containerId": "YOUR_CONTAINER_ID",
            "tagId": "1",
            "name": "GA4 - Configuration",
            "type": "gcs",
            "parameter": [
                {"type": "TEMPLATE", "key": "configId", "value": "{{GA4 Configuration}}"}
            ],
            "firingTriggerId": ["1"],  # All Pages trigger
            "tagFiringOption": "ONCE_PER_EVENT"
        })
        
        # GA4 Page View tag
        tags.append({
            "accountId": "YOUR_ACCOUNT_ID",
            "containerId": "YOUR_CONTAINER_ID",
            "tagId": "2",
            "name": "GA4 - Page View",
            "type": "gev",
            "parameter": [
                {"type": "TEMPLATE", "key": "measurementId", "value": "{{GA4 Configuration}}"},
                {"type": "TEMPLATE", "key": "eventName", "value": "page_view"}
            ],
            "firingTriggerId": ["1"],  # All Pages trigger
            "tagFiringOption": "ONCE_PER_EVENT"
        })
        
        tag_id = 3
        opportunities = analysis_result.get('conversion_opportunities', {}).get('opportunities', [])
        
        # E-commerce tags
        if any(opp['type'] == 'ecommerce' for opp in opportunities):
            ecommerce_tags = [
                {"name": "GA4 - View Item", "event": "view_item", "trigger_name": "View Item"},
                {"name": "GA4 - Add to Cart", "event": "add_to_cart", "trigger_name": "Add to Cart"},
                {"name": "GA4 - Begin Checkout", "event": "begin_checkout", "trigger_name": "Begin Checkout"},
                {"name": "GA4 - Purchase", "event": "purchase", "trigger_name": "Purchase"}
            ]
            
            for tag in ecommerce_tags:
                # Find trigger ID
                trigger_id = next((t["triggerId"] for t in triggers if t["name"] == tag["trigger_name"]), None)
                
                tags.append({
                    "accountId": "YOUR_ACCOUNT_ID",
                    "containerId": "YOUR_CONTAINER_ID",
                    "tagId": str(tag_id),
                    "name": tag["name"],
                    "type": "gev",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementId", "value": "{{GA4 Configuration}}"},
                        {"type": "TEMPLATE", "key": "eventName", "value": tag["event"]},
                        {"type": "MAP", "key": "eventParameters", "map": [
                            {"type": "TEMPLATE", "key": "currency", "value": "{{DLV - Currency}}"},
                            {"type": "TEMPLATE", "key": "value", "value": "{{DLV - Value}}"},
                            {"type": "TEMPLATE", "key": "item_id", "value": "{{DLV - Item ID}}"},
                            {"type": "TEMPLATE", "key": "item_name", "value": "{{DLV - Item Name}}"},
                            {"type": "TEMPLATE", "key": "item_category", "value": "{{DLV - Item Category}}"},
                            {"type": "TEMPLATE", "key": "quantity", "value": "{{DLV - Quantity}}"}
                        ]}
                    ],
                    "firingTriggerId": [trigger_id] if trigger_id else [],
                    "tagFiringOption": "ONCE_PER_EVENT"
                })
                tag_id += 1
        
        # Lead generation tags
        if any(opp['type'] == 'lead_generation' for opp in opportunities):
            lead_tags = [
                {"name": "GA4 - Form Submit", "event": "form_submit", "trigger_name": "Form Submit - All"},
                {"name": "GA4 - Lead Generated", "event": "generate_lead", "trigger_name": "Lead Generated"}
            ]
            
            for tag in lead_tags:
                trigger_id = next((t["triggerId"] for t in triggers if t["name"] == tag["trigger_name"]), None)
                
                tags.append({
                    "accountId": "YOUR_ACCOUNT_ID",
                    "containerId": "YOUR_CONTAINER_ID",
                    "tagId": str(tag_id),
                    "name": tag["name"],
                    "type": "gev",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementId", "value": "{{GA4 Configuration}}"},
                        {"type": "TEMPLATE", "key": "eventName", "value": tag["event"]},
                        {"type": "MAP", "key": "eventParameters", "map": [
                            {"type": "TEMPLATE", "key": "form_name", "value": "{{DLV - Form Name}}"},
                            {"type": "TEMPLATE", "key": "form_id", "value": "{{DLV - Form ID}}"},
                            {"type": "TEMPLATE", "key": "lead_type", "value": "{{DLV - Lead Type}}"}
                        ]}
                    ],
                    "firingTriggerId": [trigger_id] if trigger_id else [],
                    "tagFiringOption": "ONCE_PER_EVENT"
                })
                tag_id += 1
        
        # File download tag
        if any(opp['type'] == 'file_download' for opp in opportunities):
            trigger_id = next((t["triggerId"] for t in triggers if t["name"] == "File Download"), None)
            
            tags.append({
                "accountId": "YOUR_ACCOUNT_ID",
                "containerId": "YOUR_CONTAINER_ID",
                "tagId": str(tag_id),
                "name": "GA4 - File Download",
                "type": "gev",
                "parameter": [
                    {"type": "TEMPLATE", "key": "measurementId", "value": "{{GA4 Configuration}}"},
                    {"type": "TEMPLATE", "key": "eventName", "value": "file_download"},
                    {"type": "MAP", "key": "eventParameters", "map": [
                        {"type": "TEMPLATE", "key": "file_name", "value": "{{Click URL}}"},
                        {"type": "TEMPLATE", "key": "link_text", "value": "{{Click Text}}"}
                    ]}
                ],
                "firingTriggerId": [trigger_id] if trigger_id else [],
                "tagFiringOption": "ONCE_PER_EVENT"
            })
            tag_id += 1
        
        # Phone click tag
        if any(opp['type'] == 'phone_tracking' for opp in opportunities):
            trigger_id = next((t["triggerId"] for t in triggers if t["name"] == "Phone Click"), None)
            
            tags.append({
                "accountId": "YOUR_ACCOUNT_ID",
                "containerId": "YOUR_CONTAINER_ID",
                "tagId": str(tag_id),
                "name": "GA4 - Phone Click",
                "type": "gev",
                "parameter": [
                    {"type": "TEMPLATE", "key": "measurementId", "value": "{{GA4 Configuration}}"},
                    {"type": "TEMPLATE", "key": "eventName", "value": "phone_click"},
                    {"type": "MAP", "key": "eventParameters", "map": [
                        {"type": "TEMPLATE", "key": "phone_number", "value": "{{Click URL}}"},
                        {"type": "TEMPLATE", "key": "link_text", "value": "{{Click Text}}"}
                    ]}
                ],
                "firingTriggerId": [trigger_id] if trigger_id else [],
                "tagFiringOption": "ONCE_PER_EVENT"
            })
            tag_id += 1
        
        return tags