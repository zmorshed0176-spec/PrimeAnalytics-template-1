import { useState } from 'react';
import { Navigation } from './components/Navigation';
import { Footer } from './components/Footer';
import { HomePage } from './components/HomePage';
import { ContactPage } from './components/ContactPage';
import { TermsPage } from './components/TermsPage';
import { PrivacyPage } from './components/PrivacyPage';
import { RefundPage } from './components/RefundPage';

export default function App() {
  const [currentPage, setCurrentPage] = useState('home');

  const handleNavigate = (page: string) => {
    setCurrentPage(page);
    window.scrollTo(0, 0);
  };

  const renderPage = () => {
    switch (currentPage) {
      case 'home':
        return <HomePage onNavigate={handleNavigate} />;
      case 'services':
        // Navigate to home and scroll to services section
        handleNavigate('home');
        setTimeout(() => {
          const servicesSection = document.querySelector('#services');
          if (servicesSection) {
            servicesSection.scrollIntoView({ behavior: 'smooth' });
          }
        }, 100);
        return <HomePage onNavigate={handleNavigate} />;
      case 'portfolio':
        // Navigate to home and scroll to portfolio section
        handleNavigate('home');
        setTimeout(() => {
          const portfolioSection = document.querySelector('#portfolio');
          if (portfolioSection) {
            portfolioSection.scrollIntoView({ behavior: 'smooth' });
          }
        }, 100);
        return <HomePage onNavigate={handleNavigate} />;
      case 'testimonials':
        // Navigate to home and scroll to testimonials section
        handleNavigate('home');
        setTimeout(() => {
          const testimonialsSection = document.querySelector('#testimonials');
          if (testimonialsSection) {
            testimonialsSection.scrollIntoView({ behavior: 'smooth' });
          }
        }, 100);
        return <HomePage onNavigate={handleNavigate} />;
      case 'contact':
        return <ContactPage />;
      case 'terms':
        return <TermsPage />;
      case 'privacy':
        return <PrivacyPage />;
      case 'refund':
        return <RefundPage />;
      default:
        return <HomePage onNavigate={handleNavigate} />;
    }
  };

  return (
    <div className="min-h-screen flex flex-col">
      <Navigation currentPage={currentPage} onNavigate={handleNavigate} />
      <main className="flex-1">
        {renderPage()}
      </main>
      <Footer onNavigate={handleNavigate} />
    </div>
  );
}