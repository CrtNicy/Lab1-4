# Pages and Routing

## Overview

Experiment 4 implements page routing and layout for the flight booking system frontend using React Router and modern web design principles.

## Page Structure

### Main Pages

1. Home Page
2. Flight List Page
3. Booking Page
4. User Profile Page
5. Login/Register Page

## Route Configuration

### Router Setup

```jsx
// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import HomePage from './pages/HomePage';
import FlightListPage from './pages/FlightListPage';
import BookingPage from './pages/BookingPage';
import ProfilePage from './pages/ProfilePage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={HomePage} />
        <Route path="/flights" component={FlightListPage} />
        <Route path="/booking/:flightId" component={BookingPage} />
        <Route path="/profile" component={ProfilePage} />
        <Route path="/login" component={LoginPage} />
        <Route path="/register" component={RegisterPage} />
      </Switch>
    </Router>
  );
}

export default App;
```

## Page Components

### Home Page

```jsx
// HomePage.js
import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div className="home-page">
      <header>
        <h1>Welcome to Flight Booking System</h1>
      </header>
      <main>
        <section className="search-section">
          <h2>Find Your Flight</h2>
          <Link to="/flights" className="cta-button">
            Search Flights
          </Link>
        </section>
      </main>
    </div>
  );
}

export default HomePage;
```

### Flight List Page

```jsx
// FlightListPage.js
import React from 'react';
import FlightList from '../components/FlightList';
import SearchFilter from '../components/SearchFilter';

function FlightListPage() {
  return (
    <div className="flight-list-page">
      <h1>Available Flights</h1>
      <SearchFilter />
      <FlightList />
    </div>
  );
}

export default FlightListPage;
```

### Booking Page

```jsx
// BookingPage.js
import React from 'react';
import { useParams } from 'react-router-dom';
import BookingForm from '../components/BookingForm';
import FlightDetails from '../components/FlightDetails';

function BookingPage() {
  const { flightId } = useParams();

  return (
    <div className="booking-page">
      <h1>Flight Booking</h1>
      <FlightDetails flightId={flightId} />
      <BookingForm flightId={flightId} />
    </div>
  );
}

export default BookingPage;
```

## Page Implementation Details

### Login Page (LoginView)

The login page implements user authentication with the following features:

- Clean login form design
- Username and password validation
- Error message display
- Session persistence

### Flight List Page (FlightView)

The flight list page displays all available flights with:

- Table format flight data display
- Filtering by flight number and airline
- Flight status display (Arrival/Departure)
- Pagination functionality

### Booking Management Page (BookingView)

The booking management page is the core functionality page with:

#### Data Display
- Statistics Cards
  - Total bookings
  - Current user
  - Recent bookings

- Booking List
  - Flight number (with tags)
  - Flight type (Arrival/Departure with color coding)
  - Departure time (formatted display)
  - Passenger information (with avatar)

#### Operations
- New Booking
  - Flight number input (with validation)
  - Seat number selection (with format validation)
  - Submission confirmation

- Edit Booking
  - Seat number modification
  - Flight information retention
  - Real-time validation

- Cancellation
  - Confirmation dialog
  - Security prompt
  - Status feedback

#### User Experience
- Responsive layout
- Operation feedback
- Error handling
- Loading states
- Refresh functionality

## Code Examples

### Form Validation
```javascript
const rules = {
  flight: [
    { required: true, message: 'Please enter flight number', trigger: 'blur' },
    { min: 3, max: 10, message: 'Flight number must be 3-10 characters', trigger: 'blur' }
  ],
  seat_number: [
    { required: true, message: 'Please enter seat number', trigger: 'blur' },
    { pattern: /^[A-Z]?[0-9]+$/, message: 'Invalid seat number format', trigger: 'blur' }
  ]
};
```

### Data Loading
```javascript
const loadBookings = () => {
  axios.get('http://127.0.0.1:8000/app/api/bookings/')
    .then(response => {
      const userBookings = response.data.filter(
        (booking: any) => booking.passenger.username === store.state.username
      );
      // Process data...
    })
    .catch(error => {
      console.error(error);
    });
};
```

## Styling

Using Element Plus component library with custom styles:

```css
.booking {
  padding: 20px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.statistics {
  margin-bottom: 20px;
}

.card-content {
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  color: #409EFF;
}
```

## API Endpoints

### Get Booking List
- Endpoint: `/app/api/bookings/`
- Method: GET
- Response: List of bookings

### Create Booking
- Endpoint: `/app/api/bookings/`
- Method: POST
- Data:
  ```json
  {
    "passenger_id": 2,
    "seat_number": "A123",
    "flight": 5
  }
  ```

### Update Booking
- Endpoint: `/app/api/bookings/{id}/`
- Method: PATCH
- Data:
  ```json
  {
    "seat_number": "B456"
  }
  ```

### Delete Booking
- Endpoint: `/app/api/bookings/{id}/`
- Method: DELETE 