import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { 
  Mail, 
  Phone, 
  MapPin, 
  Calendar, 
  MessageSquare, 
  Clock,
  CheckCircle,
  Zap
} from 'lucide-react';

export function ContactPage() {
  const contactMethods = [
    {
      icon: <Mail className="h-6 w-6 text-[#4ECDC4]" />,
      title: "Email Us",
      description: "Get in touch via email",
      details: "hello@primeanalytics.com",
      action: "Send Email",
      link: "mailto:hello@primeanalytics.com"
    },
    {
      icon: <Phone className="h-6 w-6 text-[#2A6F97]" />,
      title: "Call Us",
      description: "Speak directly with our team",
      details: "+1 (555) 123-4567",
      action: "Call Now",
      link: "tel:+15551234567"
    },
    {
      icon: <Calendar className="h-6 w-6 text-[#61A5C2]" />,
      title: "Book a Call",
      description: "Schedule a discovery call",
      details: "Available Mon-Fri, 9 AM - 6 PM EST",
      action: "Book on Calendly",
      link: "https://calendly.com/primeanalytics"
    }
  ];

  const faqs = [
    {
      question: "How quickly can you audit my current setup?",
      answer: "Most analytics audits are completed within 48-72 hours. You'll receive a detailed report with actionable recommendations."
    },
    {
      question: "Do you work with agencies or direct clients?",
      answer: "Both! We specialize in serving marketing agencies as an outsourced analytics partner, and also work directly with e-commerce brands and B2B companies."
    },
    {
      question: "What platforms do you integrate with?",
      answer: "We work with all major platforms including Google Analytics 4, Google Ads, Meta (Facebook), TikTok, Shopify, HubSpot, Salesforce, and many more."
    },
    {
      question: "Are your implementations GDPR compliant?",
      answer: "Absolutely. All our implementations include proper consent management and comply with GDPR, CCPA, and other privacy regulations."
    }
  ];

  return (
    <div className="min-h-screen py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Header */}
        <div className="text-center space-y-4 mb-16">
          <h1 className="text-4xl lg:text-5xl text-[#0F3A49]">
            Get In Touch
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Ready to transform your analytics? Let's discuss how we can help you achieve 
            better tracking, clearer attribution, and measurable growth.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
          
          {/* Contact Form */}
          <div className="lg:col-span-2">
            <Card className="hover:shadow-lg transition-shadow">
              <CardHeader>
                <CardTitle className="flex items-center space-x-2 text-[#0F3A49]">
                  <MessageSquare className="h-5 w-5 text-[#4ECDC4]" />
                  <span>Send Us a Message</span>
                </CardTitle>
                <p className="text-gray-600">
                  Fill out the form below and we'll get back to you within 24 hours.
                </p>
              </CardHeader>
              <CardContent>
                {/* JotForm Embed */}
                <div className="w-full">
                  <iframe
                    id="JotFormIFrame-primeanalytics-contact"
                    title="Contact PrimeAnalytics"
                    src="https://form.jotform.com/placeholder-form-id"
                    width="100%"
                    height="600"
                    style={{
                      minWidth: '100%',
                      height: '600px',
                      border: 'none'
                    }}
                  />
                </div>
                
                {/* Fallback Contact Form UI */}
                <div className="space-y-6 bg-[#E0F8F7] p-6 rounded-lg border border-[#4ECDC4]/20 mt-4">
                  <div className="text-center space-y-2">
                    <h3 className="text-lg font-semibold text-[#0F3A49]">Alternative Contact Methods</h3>
                    <p className="text-sm text-gray-600">
                      If the form above doesn't load, you can reach us through these methods:
                    </p>
                  </div>
                  
                  <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    {contactMethods.map((method, index) => (
                      <div key={index} className="text-center space-y-2">
                        <div className="flex justify-center">{method.icon}</div>
                        <div className="text-sm font-medium text-[#0F3A49]">{method.title}</div>
                        <div className="text-xs text-gray-600">{method.details}</div>
                        <Button
                          size="sm"
                          variant="outline"
                          className="w-full border-[#4ECDC4] text-[#0F3A49] hover:bg-[#4ECDC4] hover:text-white"
                          onClick={() => window.open(method.link, '_blank')}
                        >
                          {method.action}
                        </Button>
                      </div>
                    ))}
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Sidebar */}
          <div className="space-y-8">
            
            {/* Quick Actions */}
            <Card className="hover:shadow-lg transition-shadow">
              <CardHeader>
                <CardTitle className="text-lg text-[#0F3A49]">Quick Actions</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <Button 
                  className="w-full bg-[#4ECDC4] hover:bg-[#3BB8B0] text-white"
                  onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
                >
                  <Zap className="h-4 w-4 mr-2" />
                  Get Free Audit
                </Button>
                
                <Button 
                  variant="outline" 
                  className="w-full border-[#0F3A49] text-[#0F3A49] hover:bg-[#0F3A49] hover:text-white"
                  onClick={() => window.scrollTo({ top: document.documentElement.scrollHeight, behavior: 'smooth' })}
                >
                  <Calendar className="h-4 w-4 mr-2" />
                  Book Discovery Call
                </Button>
                
                <div className="text-center pt-2">
                  <div className="flex items-center justify-center space-x-2 text-sm text-gray-600">
                    <Clock className="h-4 w-4 text-[#4ECDC4]" />
                    <span>Response within 24 hours</span>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Contact Information */}
            <Card className="hover:shadow-lg transition-shadow">
              <CardHeader>
                <CardTitle className="text-lg text-[#0F3A49]">Contact Information</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="space-y-3">
                  <div className="flex items-center space-x-3">
                    <Mail className="h-4 w-4 text-[#4ECDC4]" />
                    <span className="text-sm">hello@primeanalytics.com</span>
                  </div>
                  <div className="flex items-center space-x-3">
                    <Phone className="h-4 w-4 text-[#4ECDC4]" />
                    <span className="text-sm">+1 (555) 123-4567</span>
                  </div>
                  <div className="flex items-center space-x-3">
                    <MapPin className="h-4 w-4 text-[#4ECDC4]" />
                    <span className="text-sm">Remote & Global</span>
                  </div>
                  <div className="flex items-center space-x-3">
                    <Clock className="h-4 w-4 text-[#4ECDC4]" />
                    <span className="text-sm">Mon-Fri, 9 AM - 6 PM EST</span>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* What to Expect */}
            <Card className="hover:shadow-lg transition-shadow">
              <CardHeader>
                <CardTitle className="text-lg text-[#0F3A49]">What to Expect</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  <div className="flex items-start space-x-3">
                    <CheckCircle className="h-4 w-4 text-[#4ECDC4] mt-0.5" />
                    <div className="text-sm">
                      <div className="font-medium text-[#0F3A49]">Quick Response</div>
                      <div className="text-gray-600">We'll respond within 24 hours</div>
                    </div>
                  </div>
                  <div className="flex items-start space-x-3">
                    <CheckCircle className="h-4 w-4 text-[#4ECDC4] mt-0.5" />
                    <div className="text-sm">
                      <div className="font-medium text-[#0F3A49]">Free Consultation</div>
                      <div className="text-gray-600">Initial call is always free</div>
                    </div>
                  </div>
                  <div className="flex items-start space-x-3">
                    <CheckCircle className="h-4 w-4 text-[#4ECDC4] mt-0.5" />
                    <div className="text-sm">
                      <div className="font-medium text-[#0F3A49]">Custom Solution</div>
                      <div className="text-gray-600">Tailored to your specific needs</div>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>

        {/* FAQ Section */}
        <div className="mt-20">
          <div className="text-center space-y-4 mb-12">
            <h2 className="text-3xl text-[#0F3A49]">Frequently Asked Questions</h2>
            <p className="text-gray-600">Quick answers to common questions</p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {faqs.map((faq, index) => (
              <Card key={index} className="hover:shadow-lg transition-shadow hover:border-[#4ECDC4]/30">
                <CardContent className="p-6">
                  <h3 className="font-semibold text-[#0F3A49] mb-2">{faq.question}</h3>
                  <p className="text-gray-600 text-sm leading-relaxed">{faq.answer}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}