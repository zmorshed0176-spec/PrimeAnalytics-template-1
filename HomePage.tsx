import { Button } from './ui/button';
import { Card, CardContent } from './ui/card';
import { Badge } from './ui/badge';
import { 
  BarChart3, 
  Target, 
  Shield, 
  Zap, 
  CheckCircle, 
  ArrowRight,
  TrendingUp,
  Users,
  Award,
  Star
} from 'lucide-react';
import { ImageWithFallback } from './figma/ImageWithFallback';

interface HomePageProps {
  onNavigate: (page: string) => void;
}

export function HomePage({ onNavigate }: HomePageProps) {
  const services = [
    {
      icon: <BarChart3 className="h-8 w-8 text-[#4ECDC4]" />,
      title: "GA4 & GTM Architecture",
      description: "I design and implement comprehensive Google Analytics 4 and Google Tag Manager setups that form the backbone of your data ecosystem. This includes custom event taxonomy, enhanced e-commerce tracking, audience segmentation, and cross-domain measurement. I configure advanced features like custom dimensions, calculated metrics, and automated reporting to ensure you capture every meaningful interaction.",
      value: "Why it matters: Without proper GA4 foundation, you're flying blind. Clean data architecture means accurate attribution, reliable reporting, and confident decision-making that can improve ROAS by 25-40%."
    },
    {
      icon: <Zap className="h-8 w-8 text-[#2A6F97]" />,
      title: "Server-Side Tracking Implementation",
      description: "I deploy and configure Google Tag Manager Server-Side containers, implement Meta Conversions API (CAPI), Google Enhanced Conversions, and TikTok Events API. This includes setting up secure data pipelines, implementing first-party data enrichment, and ensuring iOS 14.5+ resilient tracking that bypasses browser limitations and ad blockers.",
      value: "Why it matters: Server-side tracking recovers 15-30% of lost conversion data from iOS updates and privacy changes. It's the difference between guessing and knowing your true ROAS, especially critical for scaling ad spend confidently."
    },
    {
      icon: <Target className="h-8 w-8 text-[#61A5C2]" />,
      title: "Conversion Tracking & Attribution",
      description: "I implement sophisticated multi-touch attribution models that track the complete customer journey across all touchpoints. This includes setting up enhanced e-commerce tracking, offline conversion imports, call tracking integration, and custom attribution windows. I configure cross-platform audience syncing and implement UTM parameter strategies for crystal-clear channel performance.",
      value: "Why it matters: Accurate attribution prevents budget waste on underperforming channels and identifies hidden revenue drivers. Clients typically discover 20-40% more value from previously 'unprofitable' campaigns."
    },
    {
      icon: <TrendingUp className="h-8 w-8 text-[#0F3A49]" />,
      title: "E-commerce & Lead-Gen Analytics",
      description: "I specialize in advanced Shopify tracking implementations including customer lifetime value calculation, product performance analysis, and cart abandonment recovery tracking. For B2B companies, I set up lead scoring, multi-stage funnel tracking, CRM integration, and marketing qualified lead (MQL) identification systems that connect marketing efforts to actual revenue.",
      value: "Why it matters: Detailed e-commerce and lead analytics reveal optimization opportunities worth thousands monthly. Understanding true customer value and lead quality transforms marketing from cost center to profit driver."
    },
    {
      icon: <Shield className="h-8 w-8 text-[#4ECDC4]" />,
      title: "Privacy Compliance & Consent Management",
      description: "I implement comprehensive GDPR and CCPA compliant tracking solutions using Google Consent Mode v2, OneTrust, or Cookiebot integration. This includes setting up consent-driven measurement, implementing data retention policies, and ensuring all tracking respects user privacy choices while maintaining data quality through modeled conversions and consent-driven attribution.",
      value: "Why it matters: Privacy compliance isn't optional—it's business protection. Proper implementation prevents costly fines while maintaining 80-90% of your analytics data quality, ensuring legal safety without sacrificing performance insights."
    }
  ];

  const stats = [
    { number: "150+", label: "Clients Served", icon: <Users className="h-6 w-6" /> },
    { number: "4.8/5", label: "Client Rating", icon: <Star className="h-6 w-6" /> },
    { number: "98%", label: "Data Accuracy", icon: <Target className="h-6 w-6" /> },
    { number: "50M+", label: "Events Tracked", icon: <BarChart3 className="h-6 w-6" /> }
  ];

  const testimonials = [
    {
      name: "Sarah Johnson",
      role: "Marketing Director, TechCorp Agency",
      content: "PrimeAnalytics transformed our client reporting. Their GA4 implementation helped us increase client retention by 40% with crystal-clear ROI visibility.",
      rating: 5
    },
    {
      name: "Mike Chen",
      role: "E-commerce Manager, RetailPlus",
      content: "The server-side tracking setup they built for our Shopify store improved our conversion data accuracy by 35%. Game-changing for our ad optimization.",
      rating: 5
    },
    {
      name: "Emily Rodriguez",
      role: "CMO, LeadGen Pro",
      content: "Their multi-touch attribution model revealed hidden conversion paths worth $200K+ in previously unattributed revenue. Exceptional technical expertise.",
      rating: 5
    }
  ];

  const portfolioItems = [
    {
      title: "7-Figure Shopify Store Optimization",
      description: "Enhanced conversion tracking and attribution for a fashion e-commerce brand, resulting in 28% improvement in ROAS.",
      tags: ["Shopify", "GA4", "Meta CAPI", "Google Ads"],
      results: "+28% ROAS, +35% Data Accuracy"
    },
    {
      title: "Marketing Agency Analytics Overhaul",
      description: "Complete GA4 and GTM restructure for a 50-client digital agency, enabling white-label reporting and client retention.",
      tags: ["GTM", "Looker Studio", "Multi-Client", "Automation"],
      results: "+40% Client Retention, 80% Time Savings"
    },
    {
      title: "B2B Lead Attribution System",
      description: "Custom multi-touch attribution model for SaaS company tracking leads across 12+ touchpoints and channels.",
      tags: ["Attribution", "CRM Integration", "B2B", "HubSpot"],
      results: "+$200K Revenue Attribution"
    }
  ];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-[#E0F8F7] to-[#B8F0ED] py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div className="space-y-8">
              <Badge variant="secondary" className="w-fit bg-white text-[#0F3A49] border-[#4ECDC4]">
                ✨ Trusted by 150+ Marketing Agencies
              </Badge>
              
              <div className="space-y-6">
                <h1 className="text-4xl lg:text-5xl text-gray-900 leading-tight">
                  Transform Your Analytics Into a 
                  <span className="text-[#0F3A49]"> Strategic Asset</span>
                </h1>
                
                <p className="text-xl text-gray-600 leading-relaxed">
                  We're the analytics experts behind successful marketing agencies and 7-8 figure e-commerce brands. 
                  Get precise tracking, clear attribution, and actionable insights that drive real growth.
                </p>
              </div>

              <div className="flex flex-col sm:flex-row gap-4">
                <Button 
                  size="lg" 
                  className="bg-[#4ECDC4] hover:bg-[#3BB8B0] text-white flex items-center space-x-2 transition-colors duration-200"
                  onClick={() => onNavigate('contact')}
                >
                  <span>Get Free Audit</span>
                  <ArrowRight className="h-4 w-4" />
                </Button>
                
                <Button 
                  size="lg" 
                  variant="outline"
                  className="border-[#0F3A49] text-[#0F3A49] hover:bg-[#0F3A49] hover:text-white"
                  onClick={() => window.scrollTo({ top: document.documentElement.scrollHeight, behavior: 'smooth' })}
                >
                  Book Discovery Call
                </Button>
              </div>

              <div className="flex items-center space-x-4 text-sm text-gray-500">
                <CheckCircle className="h-4 w-4 text-[#4ECDC4]" />
                <span>No setup fees</span>
                <CheckCircle className="h-4 w-4 text-[#4ECDC4]" />
                <span>14-day guarantee</span>
                <CheckCircle className="h-4 w-4 text-[#4ECDC4]" />
                <span>GDPR compliant</span>
              </div>
            </div>

            <div className="relative">
              <ImageWithFallback
                src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
                alt="Analytics Dashboard"
                className="rounded-lg shadow-2xl"
              />
              <div className="absolute -bottom-6 -left-6 bg-white p-4 rounded-lg shadow-lg border border-[#4ECDC4]/20">
                <div className="flex items-center space-x-3">
                  <div className="w-3 h-3 bg-[#4ECDC4] rounded-full animate-pulse"></div>
                  <span className="text-sm font-medium text-[#0F3A49]">Live Analytics Tracking</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-8">
            {stats.map((stat, index) => (
              <div key={index} className="text-center space-y-2">
                <div className="flex justify-center text-[#4ECDC4] mb-2">
                  {stat.icon}
                </div>
                <div className="text-3xl font-bold text-[#0F3A49]">{stat.number}</div>
                <div className="text-sm text-gray-600">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section id="services" className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center space-y-4 mb-16">
            <h2 className="text-3xl lg:text-4xl text-[#0F3A49]">
              Strategic Analytics Services
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              We bridge the gap between marketing objectives and technical implementation, 
              ensuring every piece of data serves a clear business purpose.
            </p>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {services.map((service, index) => (
              <Card key={index} className="p-6 hover:shadow-lg transition-shadow hover:border-[#4ECDC4]/30">
                <CardContent className="p-0 space-y-6">
                  <div className="flex items-center space-x-3">
                    {service.icon}
                    <h3 className="text-xl font-semibold text-[#0F3A49]">{service.title}</h3>
                  </div>
                  
                  <div className="space-y-4">
                    <div>
                      <h4 className="font-medium text-[#0F3A49] mb-2">What I Do:</h4>
                      <p className="text-gray-600 leading-relaxed text-sm">{service.description}</p>
                    </div>
                    
                    <div className="bg-[#E0F8F7] p-4 rounded-lg border-l-4 border-[#4ECDC4]">
                      <h4 className="font-medium text-[#0F3A49] mb-2">Business Impact:</h4>
                      <p className="text-gray-700 text-sm leading-relaxed">{service.value}</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>

          <div className="text-center mt-12">
            <Button 
              size="lg"
              onClick={() => onNavigate('contact')}
              className="bg-[#0F3A49] hover:bg-[#0A2D37] text-white"
            >
              Learn More About Our Services
            </Button>
          </div>
        </div>
      </section>

      {/* Portfolio Section */}
      <section id="portfolio" className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center space-y-4 mb-16">
            <h2 className="text-3xl lg:text-4xl text-[#0F3A49]">
              Client Success Stories
            </h2>
            <p className="text-xl text-gray-600">
              Real results from real implementations
            </p>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {portfolioItems.map((item, index) => (
              <Card key={index} className="hover:shadow-lg transition-shadow hover:border-[#4ECDC4]/30">
                <CardContent className="p-6 space-y-4">
                  <div className="space-y-3">
                    <h3 className="text-xl font-semibold text-[#0F3A49]">{item.title}</h3>
                    <p className="text-gray-600">{item.description}</p>
                  </div>
                  
                  <div className="flex flex-wrap gap-2">
                    {item.tags.map((tag, tagIndex) => (
                      <Badge key={tagIndex} variant="secondary" className="text-xs bg-[#E0F8F7] text-[#0F3A49]">
                        {tag}
                      </Badge>
                    ))}
                  </div>
                  
                  <div className="pt-4 border-t">
                    <div className="flex items-center space-x-2">
                      <Award className="h-4 w-4 text-[#4ECDC4]" />
                      <span className="text-sm font-medium text-[#0F3A49]">{item.results}</span>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>

          <div className="text-center mt-12">
            <Button 
              size="lg"
              onClick={() => onNavigate('contact')}
              className="bg-[#0F3A49] hover:bg-[#0A2D37] text-white"
            >
              Discuss Your Project
            </Button>
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section id="testimonials" className="py-20 bg-[#E0F8F7]">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center space-y-4 mb-16">
            <h2 className="text-3xl lg:text-4xl text-[#0F3A49]">
              What Our Clients Say
            </h2>
            <p className="text-xl text-gray-600">
              Trusted by marketing agencies and e-commerce brands worldwide
            </p>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {testimonials.map((testimonial, index) => (
              <Card key={index} className="bg-white hover:shadow-lg transition-shadow">
                <CardContent className="p-6 space-y-4">
                  <div className="flex space-x-1">
                    {[...Array(testimonial.rating)].map((_, i) => (
                      <Star key={i} className="h-4 w-4 fill-[#4ECDC4] text-[#4ECDC4]" />
                    ))}
                  </div>
                  
                  <p className="text-gray-700 italic leading-relaxed">
                    "{testimonial.content}"
                  </p>
                  
                  <div className="pt-4 border-t">
                    <div className="font-semibold text-[#0F3A49]">{testimonial.name}</div>
                    <div className="text-sm text-gray-600">{testimonial.role}</div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-r from-[#0F3A49] to-[#2A6F97]">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-8">
          <div className="space-y-4">
            <h2 className="text-3xl lg:text-4xl text-white">
              Ready to Transform Your Analytics?
            </h2>
            <p className="text-xl text-gray-200">
              Get a free analytics audit and discover opportunities to improve your tracking, 
              attribution, and ROI within 48 hours.
            </p>
          </div>

          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button 
              size="lg" 
              className="bg-[#4ECDC4] text-[#0F3A49] hover:bg-[#3BB8B0] hover:text-white transition-colors duration-200"
              onClick={() => onNavigate('contact')}
            >
              <Zap className="h-4 w-4 mr-2" />
              Get Free Audit
            </Button>
            
            <Button 
              size="lg" 
              variant="outline"
              className="border-white text-white hover:bg-white hover:text-[#0F3A49] transition-colors duration-200"
              onClick={() => onNavigate('contact')}
            >
              Contact Us
            </Button>
          </div>

          <div className="flex items-center justify-center space-x-4 text-sm text-gray-200">
            <CheckCircle className="h-4 w-4" />
            <span>No strings attached</span>
            <CheckCircle className="h-4 w-4" />
            <span>48-hour turnaround</span>
            <CheckCircle className="h-4 w-4" />
            <span>Actionable recommendations</span>
          </div>
        </div>
      </section>

      {/* Calendly Embed Section */}
      <section className="py-20 bg-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center space-y-4 mb-12">
            <h2 className="text-3xl lg:text-4xl text-[#0F3A49]">
              Book Your Discovery Call
            </h2>
            <p className="text-xl text-gray-600">
              Schedule a free 30-minute consultation to discuss your analytics needs
            </p>
          </div>
          
          <div className="bg-gray-50 rounded-lg p-8">
            <div className="w-full h-[700px] rounded-lg overflow-hidden">
              <iframe
                src="https://calendly.com/primeanalytics"
                width="100%"
                height="100%"
                style={{ border: 'none' }}
                title="Schedule a Discovery Call"
              />
            </div>
            
            {/* Fallback for when Calendly doesn't load */}
            <div className="mt-6 text-center">
              <p className="text-gray-600 mb-4">
                Having trouble with the calendar? You can also book directly:
              </p>
              <Button 
                size="lg"
                className="bg-[#4ECDC4] hover:bg-[#3BB8B0] text-white"
                onClick={() => window.open('https://calendly.com/primeanalytics', '_blank')}
              >
                Open Calendly in New Tab
              </Button>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}