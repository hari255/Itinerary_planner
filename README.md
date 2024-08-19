## PROJECT SCOPE

To suggest a user with personalized places around him to visit. 

### 1. **Project Overview:**
   - **Objective:** Build an Itinerary Planner that recommends nearby points of interest (POIs) or attractions within a 3-hour range from the user’s current location or a specified starting point.
   - **End Users:** Travelers, tourists, or anyone looking to explore nearby attractions.
   - **Key Features:** 
     - Location-based recommendations.
     - Time-based filtering (within 3 hours of travel).
     - Personalized suggestions based on user preferences.

### 2. **Requirements Gathering:**

#### **A. Functional Requirements:**
   1. **User Input:**
      - Users should input their current location or choose a starting point.
      - Option to set preferences (e.g., types of attractions, interests, mode of transportation).
      - Ability to specify the maximum travel time (default is 3 hours).
   
   2. **Data Acquisition:**
      - Integrate with APIs like Google Places, Yelp, Amadeus, etc., to fetch POI data.
      - Use mapping services (Google Maps, Mapbox) to calculate travel time.
      - Gather user data (location history, previous choices) for personalization.

   3. **Recommendation Engine:**
      - Calculate nearby attractions within a 3-hour travel range.
      - Rank attractions based on relevance, distance, user preferences, and reviews.
      - Suggest alternate routes or stops if the main attraction is too far.

   4. **Itinerary Planning:**
      - Generate a day’s itinerary based on selected attractions.
      - Provide estimated travel times, opening hours, and other relevant information.
      - Allow users to save and modify their itineraries.

   5. **User Interface:**
      - Simple, intuitive UI to display recommendations and itineraries.
      - Map view to visualize the route and attractions.
      - Detailed view for each attraction (with reviews, photos, etc.).

   6. **Notifications:**
      - Real-time notifications for nearby attractions during travel.
      - Alerts for closing times or better alternatives.

#### **B. Non-Functional Requirements:**
   1. **Performance:**
      - Fast response times for queries and recommendations.
      - Scalable to handle multiple users and large datasets.

   2. **Reliability:**
      - Ensure high availability and minimal downtime.
      - Implement fail-safes for API failures.

   3. **Security:**
      - Protect user data, especially location and preferences.
      - Implement secure API communication and user authentication.

   4. **Usability:**
      - Design for mobile-first usage (as most users will be on-the-go).
      - Ensure accessibility for all user types.

   5. **Compliance:**
      - Adhere to data privacy regulations like GDPR.

### 3. **Roadmap:**

#### **A. Planning Phase (Weeks 1-2):**
   - **Requirement Analysis:** Finalize the functional and non-functional requirements.
   - **Feasibility Study:** Evaluate the technical feasibility of the project.
   - **Technology Stack:** Decide on the tools, languages, and frameworks (e.g., Python, Flask/Django, React, Google Maps API).
   - **API Selection:** Choose the APIs for POI data and map services.
   - **Data Strategy:** Define how data will be collected, stored, and managed.

#### **B. Design Phase (Weeks 3-4):**
   - **System Architecture:** Design the system architecture, including the backend, frontend, and database.
   - **Database Design:** Structure the database to store user data, POIs, itineraries, etc.
   - **Algorithm Design:** Design the recommendation engine, including filtering and ranking algorithms.
   - **UI/UX Design:** Create wireframes and prototypes for the user interface.

#### **C. Development Phase (Weeks 5-12):**
   - **Backend Development:**
     - Set up the server and database.
     - Integrate APIs for POI data and maps.
     - Develop the recommendation engine.
   - **Frontend Development:**
     - Build the UI for user interaction.
     - Implement the map view and itinerary visualization.
   - **Integration:**
     - Connect the backend with the frontend.
     - Implement user authentication and preferences storage.

#### **D. Testing Phase (Weeks 13-15):**
   - **Unit Testing:** Test individual components for functionality.
   - **Integration Testing:** Ensure all components work seamlessly together.
   - **User Testing:** Conduct beta testing with real users to gather feedback.
   - **Performance Testing:** Ensure the system performs well under load.

#### **E. Deployment Phase (Week 16):**
   - **Deploy to Production:** Launch the application on a cloud platform.
   - **Monitoring:** Set up monitoring for performance and error tracking.
   - **User Onboarding:** Provide tutorials or guides for first-time users.

#### **F. Post-Launch (Ongoing):**
   - **Maintenance:** Regular updates and bug fixes.
   - **Feature Enhancements:** Based on user feedback, continuously improve the recommendation model and user experience.
   - **Marketing:** Promote the Itinerary Planner to attract users.

### 4. **Tools & Technologies:**
   - **Programming Languages:** Python (for backend), JavaScript (for frontend).
   - **Frameworks:** Flask/Django (backend), React/Angular (frontend).
   - **APIs:** Google Maps API, Yelp Fusion API, Amadeus API.
   - **Database:** PostgreSQL, MongoDB (for storing user data and POIs).
   - **Cloud Services:** AWS, GCP, or Azure for hosting.
   - **Version Control:** Git and GitHub for code management.


## Data Colelction


## Metrics
Destinations, Near by attractions, Reviews, Culture, Food preferences, Budget, No of days, No of people, Accommodation, transport,

-- Need to add more.


## Database 
MySQL/ Postgres

## Data Ingestion

### Sources

**APIs**

 - https://developers.amadeus.com/


## Data Modeling 

## Data Cleaning

## Data Analysis

## Transformations




airlines data

https://www.bts.gov/topics/airlines-and-airports/quick-links-popular-air-carrier-statistics
