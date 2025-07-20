import { Mail, Phone, MapPin, Linkedin, Twitter } from 'lucide-react';
import logoImage from 'figma:asset/65bedabc6697c8521fc253709072c2bd4879b357.png';

interface FooterProps {
  onNavigate: (page: string) => void;
}

export function Footer({ onNavigate }: FooterProps) {
  const services = [
    'GA4 & GTM Architecture',
    'Conversion Tracking',
    'E-commerce Analytics',
    'Privacy Compliance',
    'Custom Reporting'
  ];

  const legalPages = [
    { id: 'terms', label: 'Terms & Conditions' },
    { id: 'privacy', label: 'Privacy Policy' },
    { id: 'refund', label: 'Refund Policy' }
  ];

  return (
    <footer className="bg-[#0F3A49] text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          
          {/* Company Info */}
          <div className="space-y-4">
            <div className="flex items-center">
              <img 
                src={logoImage} 
                alt="PrimeAnalytics Solutions" 
                className="h-8 w-auto brightness-0 invert"
              />
            </div>
            <p className="text-gray-300 text-sm leading-relaxed">
              Specialized digital analytics consultancy driving measurable growth through data-driven insights and strategic optimization.
            </p>
            <div className="flex space-x-4">
              <Linkedin className="h-5 w-5 text-gray-400 hover:text-[#4ECDC4] cursor-pointer transition-colors" />
              <Twitter className="h-5 w-5 text-gray-400 hover:text-[#4ECDC4] cursor-pointer transition-colors" />
            </div>
          </div>

          {/* Services */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Our Services</h3>
            <ul className="space-y-2">
              {services.map((service, index) => (
                <li key={index}>
                  <button 
                    onClick={() => onNavigate('services')}
                    className="text-gray-300 hover:text-[#4ECDC4] text-sm transition-colors"
                  >
                    {service}
                  </button>
                </li>
              ))}
            </ul>
          </div>

          {/* Quick Links */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Quick Links</h3>
            <ul className="space-y-2">
              <li>
                <button 
                  onClick={() => onNavigate('home')}
                  className="text-gray-300 hover:text-[#4ECDC4] text-sm transition-colors"
                >
                  Home
                </button>
              </li>
              <li>
                <button 
                  onClick={() => onNavigate('portfolio')}
                  className="text-gray-300 hover:text-[#4ECDC4] text-sm transition-colors"
                >
                  Portfolio
                </button>
              </li>
              <li>
                <button 
                  onClick={() => onNavigate('contact')}
                  className="text-gray-300 hover:text-[#4ECDC4] text-sm transition-colors"
                >
                  Contact Us
                </button>
              </li>
              <li>
                <button 
                  onClick={() => window.open('https://calendly.com/primeanalytics', '_blank')}
                  className="text-gray-300 hover:text-[#4ECDC4] text-sm transition-colors"
                >
                  Book Free Audit
                </button>
              </li>
            </ul>
          </div>

          {/* Contact Info */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Contact Info</h3>
            <div className="space-y-3">
              <div className="flex items-center space-x-3">
                <Mail className="h-4 w-4 text-[#4ECDC4]" />
                <span className="text-gray-300 text-sm">hello@primeanalytics.com</span>
              </div>
              <div className="flex items-center space-x-3">
                <Phone className="h-4 w-4 text-[#4ECDC4]" />
                <span className="text-gray-300 text-sm">+1 (555) 123-4567</span>
              </div>
              <div className="flex items-center space-x-3">
                <MapPin className="h-4 w-4 text-[#4ECDC4]" />
                <span className="text-gray-300 text-sm">Remote & Global</span>
              </div>
            </div>
          </div>
        </div>

        {/* Bottom Section */}
        <div className="border-t border-[#2A6F97] mt-8 pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
            <div className="text-gray-400 text-sm">
              © 2025 PrimeAnalytics Solutions. All rights reserved.
            </div>
            <div className="flex space-x-6">
              {legalPages.map((page) => (
                <button
                  key={page.id}
                  onClick={() => onNavigate(page.id)}
                  className="text-gray-400 hover:text-[#4ECDC4] text-sm transition-colors"
                >
                  {page.label}
                </button>
              ))}
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}