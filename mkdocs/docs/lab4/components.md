# React Components

## Overview

Experiment 4 implements various React components for the flight booking system frontend. These components provide a modern, interactive user interface for managing flights, bookings, and user interactions.

## Component Structure

### App Component

```jsx
// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navigation from './components/Navigation';
import FlightList from './components/FlightList';
import BookingForm from './components/BookingForm';
import UserProfile from './components/UserProfile';

function App() {
  return (
    <Router>
      <div className="app">
        <Navigation />
        <Switch>
          <Route exact path="/" component={FlightList} />
          <Route path="/booking/:flightId" component={BookingForm} />
          <Route path="/profile" component={UserProfile} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
```

### Navigation Component

```jsx
// Navigation.js
import React from 'react';
import { Link } from 'react-router-dom';

function Navigation() {
  return (
    <nav className="navigation">
      <Link to="/">Flights</Link>
      <Link to="/profile">My Profile</Link>
    </nav>
  );
}

export default Navigation;
```

### Flight List Component

```jsx
// FlightList.js
import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import FlightCard from './FlightCard';

function FlightList() {
  const [flights, setFlights] = useState([]);
  const history = useHistory();

  useEffect(() => {
    fetchFlights();
  }, []);

  const fetchFlights = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/flights/');
      const data = await response.json();
      setFlights(data);
    } catch (error) {
      console.error('Error fetching flights:', error);
    }
  };

  const handleBooking = (flightId) => {
    history.push(`/booking/${flightId}`);
  };

  return (
    <div className="flight-list">
      {flights.map(flight => (
        <FlightCard
          key={flight.id}
          flight={flight}
          onBook={() => handleBooking(flight.id)}
        />
      ))}
    </div>
  );
}

export default FlightList;
```

### Flight Card Component

```jsx
// FlightCard.js
import React from 'react';

function FlightCard({ flight, onBook }) {
  return (
    <div className="flight-card">
      <h3>{flight.airline}</h3>
      <p>Flight Number: {flight.flight_number}</p>
      <p>Departure: {new Date(flight.departure_time).toLocaleString()}</p>
      <p>Arrival: {new Date(flight.arrival_time).toLocaleString()}</p>
      <p>Gate: {flight.gate_number}</p>
      <button onClick={onBook}>Book Now</button>
    </div>
  );
}

export default FlightCard;
```

### Booking Form Component

```jsx
// BookingForm.js
import React, { useState } from 'react';
import { useParams, useHistory } from 'react-router-dom';

function BookingForm() {
  const { flightId } = useParams();
  const history = useHistory();
  const [seatNumber, setSeatNumber] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/api/bookings/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          flight: flightId,
          seat_number: seatNumber,
        }),
      });
      if (response.ok) {
        history.push('/profile');
      }
    } catch (error) {
      console.error('Error creating booking:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="booking-form">
      <h2>Book Flight</h2>
      <div>
        <label>Seat Number:</label>
        <input
          type="text"
          value={seatNumber}
          onChange={(e) => setSeatNumber(e.target.value)}
          required
        />
      </div>
      <button type="submit">Confirm Booking</button>
    </form>
  );
}

export default BookingForm;
```

## Component Features

1. Routing
   - React Router integration
   - Dynamic route parameters
   - Navigation handling

2. State Management
   - useState hooks
   - useEffect for data fetching
   - Component state handling

3. API Integration
   - Fetch API usage
   - Async/await operations
   - Error handling

4. Event Handling
   - Form submissions
   - Button clicks
   - User interactions

## Component Styling

### CSS Modules

```css
/* FlightCard.module.css */
.flight-card {
  border: 1px solid #ddd;
  padding: 15px;
  margin: 10px;
  border-radius: 5px;
}

.flight-card h3 {
  margin: 0 0 10px;
  color: #333;
}

.flight-card button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
}
```

## Best Practices

1. Component Organization
   - Modular structure
   - Single responsibility
   - Reusable components

2. State Management
   - Proper state location
   - State updates
   - Props passing

3. Performance
   - Memoization
   - Lazy loading
   - Effect cleanup

4. Error Handling
   - Error boundaries
   - Loading states
   - User feedback 