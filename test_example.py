#!/usr/bin/env python3
"""
PrimeAnalytics AI Agent - Test Example
This script demonstrates how to use the analytics agent programmatically.
"""

import json
import sys
from website_analyzer import WebsiteAnalyzer
from gtm_generator import GTMGenerator
from report_generator import ReportGenerator

def test_analysis(url="https://example.com"):
    """Test the complete analysis workflow"""
    
    print(f"🔍 Starting analysis for: {url}")
    print("=" * 50)
    
    try:
        # Step 1: Analyze website
        print("Step 1: Analyzing website...")
        analyzer = WebsiteAnalyzer()
        analysis_result = analyzer.analyze(url)
        
        if 'error' in analysis_result:
            print(f"❌ Analysis failed: {analysis_result['error']}")
            return False
        
        # Step 2: Generate GTM container
        print("Step 2: Generating GTM container...")
        gtm_generator = GTMGenerator()
        gtm_json = gtm_generator.generate_container(analysis_result)
        
        # Step 3: Generate report
        print("Step 3: Generating comprehensive report...")
        report_generator = ReportGenerator()
        report = report_generator.generate_report(analysis_result, gtm_json)
        
        # Display results
        print("\n📊 ANALYSIS RESULTS")
        print("=" * 50)
        
        # Basic info
        basic_info = analysis_result.get('basic_info', {})
        print(f"Website Title: {basic_info.get('title', 'N/A')}")
        print(f"Status Code: {basic_info.get('status_code', 'N/A')}")
        print(f"Load Time: {basic_info.get('response_time', 0):.2f}s")
        
        # CMS Detection
        cms_info = analysis_result.get('cms_detection', {})
        print(f"Primary CMS: {cms_info.get('primary_cms', 'Unknown')}")
        
        # Analytics Detection
        analytics = analysis_result.get('analytics_detection', {})
        print(f"Has GTM: {'✅' if analytics.get('has_gtm') else '❌'}")
        print(f"Has GA4: {'✅' if analytics.get('has_ga4') else '❌'}")
        print(f"Has Consent Management: {'✅' if analytics.get('has_consent_management') else '❌'}")
        
        # Conversion Opportunities
        opportunities = analysis_result.get('conversion_opportunities', {})
        total_opps = opportunities.get('total_opportunities', 0)
        print(f"Conversion Opportunities: {total_opps}")
        
        if total_opps > 0:
            print("Recommended Events:")
            for event in opportunities.get('recommended_events', []):
                print(f"  • {event}")
        
        # GTM Container Info
        container_version = gtm_json.get('containerVersion', {})
        tags_count = len(container_version.get('tag', []))
        triggers_count = len(container_version.get('trigger', []))
        variables_count = len(container_version.get('variable', []))
        
        print(f"\n🛠️ GTM CONTAINER GENERATED")
        print("=" * 50)
        print(f"Tags: {tags_count}")
        print(f"Triggers: {triggers_count}")
        print(f"Variables: {variables_count}")
        
        # Audit Score
        audit_score = report.get('executive_summary', {}).get('audit_score', 0)
        print(f"\n📈 AUDIT SCORE: {audit_score}/100")
        
        # Recommendations
        recommendations = analysis_result.get('recommendations', [])
        if recommendations:
            print(f"\n💡 TOP RECOMMENDATIONS")
            print("=" * 50)
            for i, rec in enumerate(recommendations[:3], 1):
                priority = rec.get('priority', 'Medium')
                title = rec.get('title', 'No title')
                print(f"{i}. [{priority}] {title}")
        
        # Save files for inspection
        with open('example_gtm_container.json', 'w') as f:
            json.dump(gtm_json, f, indent=2)
        
        with open('example_audit_report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n✅ Analysis complete!")
        print("Files saved:")
        print("  • example_gtm_container.json")
        print("  • example_audit_report.json")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during analysis: {str(e)}")
        return False

def main():
    """Main function"""
    
    print("🚀 PrimeAnalytics AI Agent - Test Example")
    print("=" * 50)
    
    # Use URL from command line argument or default
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    
    print(f"Testing with URL: {url}")
    print("Note: This may take 30-60 seconds depending on the website...")
    print()
    
    success = test_analysis(url)
    
    if success:
        print("\n🎉 Test completed successfully!")
        print("\nNext steps:")
        print("1. Review the generated files")
        print("2. Import the GTM container JSON into your GTM account")
        print("3. Follow the implementation plan in the audit report")
        print("4. Run the web interface with: python app.py")
    else:
        print("\n❌ Test failed. Please check the error messages above.")
        print("\nTroubleshooting:")
        print("1. Ensure you have a stable internet connection")
        print("2. Try with a different URL")
        print("3. Check if Chrome browser is installed")
        print("4. Install dependencies: pip install -r requirements.txt")

if __name__ == "__main__":
    main()