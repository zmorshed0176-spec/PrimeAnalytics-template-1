from flask import Flask, render_template, request, jsonify, send_file
import os
from datetime import datetime
from website_analyzer import WebsiteAnalyzer
from gtm_generator import GTMGenerator
from report_generator import ReportGenerator
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_website():
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        # Initialize analyzer
        analyzer = WebsiteAnalyzer()
        
        # Step 1: Crawl and analyze website
        analysis_result = analyzer.analyze(url)
        
        # Step 2: Generate GTM JSON
        gtm_generator = GTMGenerator()
        gtm_json = gtm_generator.generate_container(analysis_result)
        
        # Step 3: Generate report
        report_generator = ReportGenerator()
        report = report_generator.generate_report(analysis_result, gtm_json)
        
        # Step 4: Save files
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        gtm_filename = f"gtm_container_{timestamp}.json"
        report_filename = f"audit_report_{timestamp}.json"
        
        # Save GTM JSON
        with open(f"output/{gtm_filename}", 'w') as f:
            json.dump(gtm_json, f, indent=2)
        
        # Save report
        with open(f"output/{report_filename}", 'w') as f:
            json.dump(report, f, indent=2)
        
        return jsonify({
            'success': True,
            'report': report,
            'gtm_filename': gtm_filename,
            'report_filename': report_filename
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    try:
        return send_file(f"output/{filename}", as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    # Create output directory if it doesn't exist
    os.makedirs('output', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)