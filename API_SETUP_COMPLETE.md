# Car CRUD API - Complete Setup & Usage Guide

## ✅ What's Been Implemented

I've created a fully functional **REST API** for Car CRUD operations that works with curl commands.

### Components Added:

1. **REST Framework Integration**
   - ✅ Django REST Framework installed (`djangorestframework`)
   - ✅ Added to `INSTALLED_APPS` in `Easy/settings.py`

2. **Serializer** (`app/serializers.py`)
   - ✅ `CarSerializer` for JSON conversion
   - ✅ Validation for unique registration numbers
   - ✅ Create/Update/Delete support

3. **API Views** (`app/views.py`)
   - ✅ `car_api_list()` - GET all cars, POST to create
   - ✅ `car_api_detail()` - GET specific, PUT to update, DELETE to remove
   - ✅ Permission checks (staff-only for write operations)
   - ✅ Proper HTTP status codes

4. **URL Routes** (`app/urls.py`)
   - ✅ `GET /api/cars/` - List all cars
   - ✅ `POST /api/cars/` - Create car
   - ✅ `GET /api/cars/<id>/` - Get car details
   - ✅ `PUT /api/cars/<id>/` - Update car
   - ✅ `DELETE /api/cars/<id>/` - Delete car

5. **Documentation & Scripts**
   - ✅ `CURL_API_GUIDE.md` - Comprehensive guide with examples
   - ✅ `CURL_QUICK_REFERENCE.md` - Quick commands reference
   - ✅ `test_car_crud.ps1` - Automated demo script

---

## 🚀 Getting Started

### Step 1: Start the Server
```powershell
cd c:\Users\aswin\Downloads\Drive_Easy-master\Drive_Easy-master
python manage.py runserver
```

**You should see:**
```
Starting development server at http://127.0.0.1:8000/
```

### Step 2: Ensure you have a staff/admin user
```powershell
python manage.py createsuperuser
# Create user: admin, password: your_password, etc.
```

---

## 💻 Using curl Commands

### Example 1: List All Cars

```powershell
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:password"))
curl.exe -H "Authorization: Basic $creds" `
  http://127.0.0.1:8000/api/cars/
```

**Response:**
```json
[
  {
    "id": 1,
    "category": "Ambassador",
    "ac_type": "AC",
    "total_cars": 3,
    "registration_number": "DL01AB0001",
    "price": "5000.00",
    "price_per_hour": 200,
    "price_per_km": 12.5,
    "fuel_consumption": "petrol",
    "status": "available"
  }
]
```

### Example 2: Create a New Car

```powershell
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:password"))
$json = @{
    category = "Hyundai Creta"
    ac_type = "AC"
    total_cars = 2
    registration_number = "MH02XY1234"
    price = 7500
    price_per_hour = 300
    price_per_km = 18
    fuel_consumption = "diesel"
    status = "available"
} | ConvertTo-Json

curl.exe -X POST `
  -H "Authorization: Basic $creds" `
  -H "Content-Type: application/json" `
  -d $json `
  http://127.0.0.1:8000/api/cars/
```

### Example 3: Update a Car

```powershell
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:password"))
$json = @{
    price = 8000
    total_cars = 5
} | ConvertTo-Json

curl.exe -X PUT `
  -H "Authorization: Basic $creds" `
  -H "Content-Type: application/json" `
  -d $json `
  http://127.0.0.1:8000/api/cars/6/
```

### Example 4: Delete a Car

```powershell
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:password"))
curl.exe -X DELETE `
  -H "Authorization: Basic $creds" `
  http://127.0.0.1:8000/api/cars/6/
```

---

## 🎬 Run the Demo Script

I've created an automated PowerShell script that demonstrates all CRUD operations:

```powershell
# Navigate to project root
cd c:\Users\aswin\Downloads\Drive_Easy-master\Drive_Easy-master

# Run with your credentials
.\test_car_crud.ps1 -Username admin -Password your_password
```

**What it does:**
1. ✅ Lists all cars
2. ✅ Creates a new car
3. ✅ Retrieves the created car's details
4. ✅ Updates the car's price and availability
5. ✅ Deletes the test car

**Output:**
```
╔════════════════════════════════════════════╗
║   🚗 Car Management API - CRUD Demo 🚗    ║
╚════════════════════════════════════════════╝

[Step 1/5] Listing all cars
┌─ GET /api/cars/
│  📝 Get list of all available cars
│
│  ✅ Success (Status: OK)
│  Response:
│  Count: 5 items
│    - ID: 1, Category: Ambassador
│    - ID: 2, Category: Tata Sumo
...
```

---

## 📚 Files Created/Modified

| File | Type | Purpose |
|------|------|---------|
| `app/serializers.py` | NEW | Car model serializer |
| `app/views.py` | MODIFIED | Added `car_api_list()` and `car_api_detail()` |
| `app/urls.py` | MODIFIED | Added API routes |
| `Easy/settings.py` | MODIFIED | Added `rest_framework` to INSTALLED_APPS |
| `CURL_API_GUIDE.md` | NEW | Complete API documentation |
| `CURL_QUICK_REFERENCE.md` | NEW | Quick commands reference |
| `test_car_crud.ps1` | NEW | Automated demo script |

---

## 🔐 Authentication

The API uses **HTTP Basic Authentication**:

```
Authorization: Basic <base64(username:password)>
```

### In PowerShell:
```powershell
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:password"))
curl.exe -H "Authorization: Basic $creds" http://127.0.0.1:8000/api/cars/
```

---

## 🛡️ Permissions

| Operation | Permission | Requires |
|-----------|-----------|----------|
| List cars | Any authenticated user | ❌ No staff needed |
| Get car details | Any authenticated user | ❌ No staff needed |
| Create car | Staff/Admin only | ✅ Staff user |
| Update car | Staff/Admin only | ✅ Staff user |
| Delete car | Staff/Admin only | ✅ Staff user |

---

## 🧪 Testing Tips

### 1. Test with curl directly
```powershell
# Easy one-liner (no auth required for listing)
curl.exe http://127.0.0.1:8000/api/cars/
```

### 2. Use Postman (optional)
- Import the API endpoints
- Set Authorization → Basic Auth
- Test all CRUD operations visually

### 3. Check API responses
```powershell
# View full response with headers
curl.exe -v -H "Authorization: Basic $creds" `
  http://127.0.0.1:8000/api/cars/
```

---

## 📝 API Endpoints Summary

```
GET    /api/cars/           → List all cars
POST   /api/cars/           → Create new car
GET    /api/cars/<id>/      → Get car by ID
PUT    /api/cars/<id>/      → Update car
DELETE /api/cars/<id>/      → Delete car
```

---

## ❓ Troubleshooting

### "401 Unauthorized"
- Check your username/password
- Verify base64 encoding is correct
- Ensure user exists and is active

### "403 Forbidden"
- You need a staff account for CREATE/UPDATE/DELETE
- Use `python manage.py createsuperuser` to create admin

### "404 Not Found"
- Car ID doesn't exist
- Check available IDs with: `GET /api/cars/`

### "400 Bad Request"
- Invalid JSON format
- Missing required fields
- Registration number already exists

---

## 🔗 Related Files

- **API Documentation:** `CURL_API_GUIDE.md`
- **Quick Reference:** `CURL_QUICK_REFERENCE.md`
- **Demo Script:** `test_car_crud.ps1`

---

## ✨ What's Next?

You can now:
- ✅ List, create, update, and delete cars via curl
- ✅ Automate car management tasks with scripts
- ✅ Integrate with external systems via REST API
- ✅ Test API endpoints programmatically

For more advanced features, consider:
- Adding JWT authentication
- Implementing filtering/pagination
- Adding search functionality
- Creating API documentation with Swagger

---

## System Check

✅ **Status:** All systems operational
- Django: OK (0 issues)
- REST Framework: Installed
- API Views: Ready
- Serializer: Ready
- Routes: Configured

**Ready to use!** Start the server and run your first curl command.
