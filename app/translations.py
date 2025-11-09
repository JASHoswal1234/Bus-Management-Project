# translations.py - Bilingual support for English and Marathi

TRANSLATIONS = {
    'en': {
        # Navigation
        'home': 'Home',
        'buses': 'Buses',
        'routes': 'Routes',
        'schedules': 'Schedules',
        'crew': 'Crew',
        'dashboard': 'Dashboard',
        'reports': 'Reports',

        # Home cards / buttons
        'manage_buses': 'Manage Buses',
        'manage_routes': 'Manage Routes',
        'manage_schedules': 'Manage Schedules',
        'manage_crew': 'Manage Crew',
        'view_dashboard': 'View Dashboard',
        'view_reports': 'View Reports',


        # Dashboard dropdown
        'analytics': 'Analytics',
        'live_tracking': 'Live Tracking (Operator)',
        'track_bus': 'Track Your Bus (User)',
        'live_demo': 'Live Demo',

        # Home page
        'welcome_title': 'Welcome to Bus Depot Management System',
        'welcome_subtitle': 'Efficient Fleet Management & Real-Time Tracking',
        'get_started': 'Get Started',
        'view_live_demo': 'View Live Demo',
        'about_system': 'About the System',
        'about_text': 'Our comprehensive bus management system provides real-time tracking, route optimization, crew management, and detailed analytics. Monitor your entire fleet from a single dashboard.',
        'key_features': 'Key Features',
        'feature_tracking': 'Real-Time GPS Tracking',
        'feature_tracking_desc': 'Track all buses live on interactive maps',
        'feature_management': 'Fleet Management',
        'feature_management_desc': 'Manage buses, routes, and schedules efficiently',
        'feature_analytics': 'Analytics Dashboard',
        'feature_analytics_desc': 'Comprehensive reports and visualizations',
        'feature_crew': 'Crew Management',
        'feature_crew_desc': 'Assign and track crew members',

        # Dashboard pages
        'operator_dashboard_title': 'Live Operator Dashboard',
        'active_buses': 'Active Buses',
        'total_fleet': 'Total Fleet',
        'connection_status': 'Socket.IO Status',
        'live_fleet_map': 'Live Fleet Map',
        'connecting': 'Connecting...',
        'connected': 'Connected',
        'disconnected': 'Disconnected',
        'offline_mode': 'Offline Mode',

        # User dashboard
        'track_your_bus': 'Track Your Bus',
        'select_route': 'Select Route',
        'choose_route': 'Choose a route...',
        'track_bus_btn': 'Track Bus',
        'bus_location': 'Bus Location',
        'speed': 'Speed',

        # Live demo
        'live_demo_title': 'Live Demo - Real-Time Tracking',

        # Buses module
        'add_bus': 'Add Bus',
        'edit_bus': 'Edit Bus',
        'delete_bus': 'Delete Bus',
        'bus_number': 'Bus Number',
        'capacity': 'Capacity',
        'model': 'Model',
        'status': 'Status',
        'purchase_date': 'Purchase Date',
        'active': 'Active',
        'inactive': 'Inactive',
        'maintenance': 'Maintenance',

        # Routes module
        'add_route': 'Add Route',
        'edit_route': 'Edit Route',
        'route_name': 'Route Name',
        'start_point': 'Start Point',
        'end_point': 'End Point',
        'distance': 'Distance (km)',
        'delete_route': 'Delete Route',

        # Schedules module
        'add_schedule': 'Add Schedule',
        'edit_schedule': 'Edit Schedule',
        'departure_time': 'Departure Time',
        'arrival_time': 'Arrival Time',
        'frequency': 'Frequency',
        'daily': 'Daily',
        'weekday': 'Weekday',
        'weekend': 'Weekend',
        'assign_crew': 'Assign Crew',
        'active_status': 'Active',

        # Crew module
        'add_crew': 'Add Crew Member',
        'crew_name': 'Name',
        'crew_role': 'Role',
        'driver': 'Driver',
        'conductor': 'Conductor',
        'maintenance_staff': 'Maintenance Staff',
        'contact_info': 'Contact Info',
        'hire_date': 'Hire Date',
        'assign_to_schedule': 'Assign to Schedule',

        # Reports module
        'reports_title': 'Reports & Exports',
        'daily_schedules': 'Daily Schedules Report',
        'crew_assignments': 'Crew Assignments Report',
        'route_performance': 'Route Performance Summary',
        'export_pdf': 'Export to PDF',
        'export_csv': 'Export to CSV',

        # Common
        'loading': 'Loading...',
        'error': 'Error',
        'success': 'Success',
        'no_data': 'No data available',
        'save': 'Save',
        'cancel': 'Cancel',
        'update': 'Update',
        'actions': 'Actions',
        'view': 'View',
        'edit': 'Edit',
        'delete': 'Delete',
        'confirm_delete': 'Are you sure you want to delete this item?',
    },

    'mr': {
        # Navigation
        'home': 'मुख्यपृष्ठ',
        'buses': 'बसेस',
        'routes': 'मार्ग',
        'schedules': 'वेळापत्रक',
        'crew': 'कर्मचारी',
        'dashboard': 'डॅशबोर्ड',
        'reports': 'अहवाल',

        # Home cards / buttons
        'manage_buses': 'बस व्यवस्थापित करा',
        'manage_routes': 'मार्ग व्यवस्थापित करा',
        'manage_schedules': 'वेळापत्रके व्यवस्थापित करा',
        'manage_crew': 'कर्मचारी व्यवस्थापित करा',
        'view_dashboard': 'डॅशबोर्ड पहा',
        'view_reports': 'अहवाल पहा',


        # Dashboard dropdown
        'analytics': 'विश्लेषण',
        'live_tracking': 'लाइव्ह ट्रॅकिंग (ऑपरेटर)',
        'track_bus': 'तुमची बस शोधा',
        'live_demo': 'लाइव्ह डेमो',

        # Home page
        'welcome_title': 'बस डेपो व्यवस्थापन प्रणालीमध्ये आपले स्वागत आहे',
        'welcome_subtitle': 'कार्यक्षम फ्लीट व्यवस्थापन आणि रिअल-टाइम ट्रॅकिंग',
        'get_started': 'सुरुवात करा',
        'view_live_demo': 'लाइव्ह डेमो पहा',
        'about_system': 'प्रणालीबद्दल',
        'about_text': 'आमची सर्वसमावेशक बस व्यवस्थापन प्रणाली रिअल-टाइम ट्रॅकिंग, मार्ग ऑप्टिमायझेशन, कर्मचारी व्यवस्थापन आणि तपशीलवार विश्लेषण प्रदान करते. एका डॅशबोर्डवरून तुमचा संपूर्ण ताफा मॉनिटर करा.',
        'key_features': 'मुख्य वैशिष्ट्ये',
        'feature_tracking': 'रिअल-टाइम GPS ट्रॅकिंग',
        'feature_tracking_desc': 'इंटरॅक्टिव्ह नकाशांवर सर्व बसेस लाइव्ह ट्रॅक करा',
        'feature_management': 'फ्लीट व्यवस्थापन',
        'feature_management_desc': 'बसेस, मार्ग आणि वेळापत्रक कार्यक्षमतेने व्यवस्थापित करा',
        'feature_analytics': 'विश्लेषण डॅशबोर्ड',
        'feature_analytics_desc': 'सर्वसमावेशक अहवाल आणि व्हिज्युअलायझेशन',
        'feature_crew': 'कर्मचारी व्यवस्थापन',
        'feature_crew_desc': 'कर्मचारी सदस्य नियुक्त करा आणि ट्रॅक करा',

        # Dashboard pages
        'operator_dashboard_title': 'लाइव्ह ऑपरेटर डॅशबोर्ड',
        'active_buses': 'सक्रिय बसेस',
        'total_fleet': 'एकूण ताफा',
        'connection_status': 'कनेक्शन स्थिती',
        'live_fleet_map': 'लाइव्ह फ्लीट नकाशा',
        'connecting': 'कनेक्ट होत आहे...',
        'connected': 'कनेक्ट केले',
        'disconnected': 'डिस्कनेक्ट केले',
        'offline_mode': 'ऑफलाइन मोड',

        # User dashboard
        'track_your_bus': 'तुमची बस शोधा',
        'select_route': 'मार्ग निवडा',
        'choose_route': 'मार्ग निवडा...',
        'track_bus_btn': 'बस ट्रॅक करा',
        'bus_location': 'बस स्थान',
        'speed': 'वेग',

        # Live demo
        'live_demo_title': 'लाइव्ह डेमो - रिअल-टाइम ट्रॅकिंग',

        # Buses module
        'add_bus': 'नवीन बस जोडा',
        'edit_bus': 'बस संपादित करा',
        'delete_bus': 'बस हटवा',
        'bus_number': 'बस क्रमांक',
        'capacity': 'क्षमता',
        'model': 'मॉडेल',
        'status': 'स्थिती',
        'purchase_date': 'खरेदी दिनांक',
        'active': 'सक्रिय',
        'inactive': 'निष्क्रिय',
        'maintenance': 'देखभाल',

        # Routes module
        'add_route': 'नवीन मार्ग जोडा',
        'edit_route': 'मार्ग संपादित करा',
        'route_name': 'मार्गाचे नाव',
        'start_point': 'प्रारंभ बिंदू',
        'end_point': 'शेवटचा बिंदू',
        'distance': 'अंतर (किमी)',
        'delete_route': 'मार्ग हटवा',

        # Schedules module
        'add_schedule': 'वेळापत्रक जोडा',
        'edit_schedule': 'वेळापत्रक संपादित करा',
        'departure_time': 'प्रस्थान वेळ',
        'arrival_time': 'पोचण्याची वेळ',
        'frequency': 'वारंवारता',
        'daily': 'दररोज',
        'weekday': 'सप्ताहातील दिवस',
        'weekend': 'सप्ताहांत',
        'assign_crew': 'कर्मचारी नियुक्त करा',
        'active_status': 'सक्रिय स्थिती',

        # Crew module
        'add_crew': 'नवीन कर्मचारी जोडा',
        'crew_name': 'नाव',
        'crew_role': 'भूमिका',
        'driver': 'चालक',
        'conductor': 'वाहक',
        'maintenance_staff': 'देखभाल कर्मचारी',
        'contact_info': 'संपर्क माहिती',
        'hire_date': 'भरती दिनांक',
        'assign_to_schedule': 'वेळापत्रकासाठी नियुक्त करा',

        # Reports module
        'reports_title': 'अहवाल आणि निर्यात',
        'daily_schedules': 'दैनिक वेळापत्रक अहवाल',
        'crew_assignments': 'कर्मचारी नियुक्ती अहवाल',
        'route_performance': 'मार्ग कार्यप्रदर्शन सारांश',
        'export_pdf': 'PDF मध्ये निर्यात करा',
        'export_csv': 'CSV मध्ये निर्यात करा',

        # Common
        'loading': 'लोड होत आहे...',
        'error': 'त्रुटी',
        'success': 'यशस्वी',
        'no_data': 'डेटा उपलब्ध नाही',
        'save': 'जतन करा',
        'cancel': 'रद्द करा',
        'update': 'अद्यतनित करा',
        'actions': 'क्रिया',
        'view': 'पहा',
        'edit': 'संपादित करा',
        'delete': 'हटवा',
        'confirm_delete': 'आपल्याला ही नोंद हटवायची खात्री आहे का?',
    }
}


def get_translation(key, lang='en'):
    """Get translation for a key in specified language (fallbacks to English)."""
    return TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(key, TRANSLATIONS['en'].get(key, key))
