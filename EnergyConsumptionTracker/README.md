EnergyConsumptionTracker/
├── backend/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── console.py
│   ├── requirements.txt
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── energy_record.py
│   │   ├── analytics.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── energy.py
│   │   ├── user.py
│   │   ├── analytics.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_auth.py
│   │   ├── test_energy.py
│   │   ├── test_user.py
│   │   ├── test_analytics.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── token.py
├── frontend/
│   ├── public/
│   │   ├── index.html
│   ├── src/
│   │   ├── api.js
│   │   ├── App.css
│   │   ├── App.js
│   │   ├── components/
│   │   │   ├── EnergyRecordList.js
│   │   │   ├── EnergyRecordForm.js
│   │   │   ├── LoginForm.js
│   │   │   ├── RegisterForm.js
│   │   │   ├── Analytics.js
│   │   ├── index.css
│   │   ├── index.js
│   │   ├── services/
│   │   │   ├── authService.js
│   │   │   ├── energyService.js
│   │   │   ├── analyticsService.js
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
├── .gitlab-ci.yml
├── README.md

