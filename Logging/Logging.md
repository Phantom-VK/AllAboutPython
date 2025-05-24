Here's a **comprehensive guide** to Python logging with detailed explanations of your code and best practices:

---

### **1. Core Logging Concepts**
```python
import logging

# Create loggers for different modules
logger1 = logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger("module2")
logger2.setLevel(logging.WARNING)

logger3 = logging.getLogger("module3")
logger3.setLevel(logging.INFO)

# Basic configuration (global)
logging.basicConfig(
    # filename='app.log',  # Uncomment to log to file
    # filemode='a',        # 'a'=append (default), 'w'=overwrite
    level=logging.DEBUG,   # Global minimum log level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

# Example log messages
logger3.info("Info message for module3")
logger1.debug("Debug message for module1")
logger2.warning("Warning message for module2")
logger3.error("Error message for module3")
```

---

### **2. Key Components Explained**

#### **A. Loggers**
- **Purpose**: Channel for emitting log messages
- **Hierarchy**: Dot-separated names (e.g., `module1.submodule`)
- **Levels** (ascending severity):
  ```python
  logging.DEBUG    # Detailed info (development)
  logging.INFO     # Confirmation of things working
  logging.WARNING  # Unexpected but handled events
  logging.ERROR    # Serious problems
  logging.CRITICAL # Critical failures
  ```

#### **B. Handlers**
Send logs to different destinations:
```python
# Add to your configuration:
file_handler = logging.FileHandler('module1.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
logger1.addHandler(file_handler)
```

#### **C. Formatters**
Structure log messages:
```python
formatter = logging.Formatter(
    '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
```

#### **D. Filters**
Advanced message filtering:
```python
class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO

logger1.addFilter(InfoFilter())
```

---

### **3. Best Practices**

#### **Logger Naming**
```python
# Good (use __name__ for automatic module naming)
logger = logging.getLogger(__name__)

# Avoid
logger = logging.getLogger("arbitrary_name")
```

#### **Configuration Approaches**
1. **Basic (Simple Apps)**:
   ```python
   logging.basicConfig(level=logging.INFO)
   ```

2. **DictConfig (Recommended)**:
   ```python
   import logging.config

   LOGGING_CONFIG = {
       'version': 1,
       'formatters': {
           'detailed': {
               'format': '%(asctime)s %(name)-15s %(levelname)-8s %(message)s'
           }
       },
       'handlers': {
           'console': {
               'class': 'logging.StreamHandler',
               'level': 'INFO',
               'formatter': 'detailed'
           },
           'file': {
               'class': 'logging.FileHandler',
               'filename': 'app.log',
               'level': 'DEBUG',
               'formatter': 'detailed'
           }
       },
       'root': {
           'level': 'DEBUG',
           'handlers': ['console', 'file']
       }
   }

   logging.config.dictConfig(LOGGING_CONFIG)
   ```

#### **Logging in Modules**
`module.py`:
```python
import logging
logger = logging.getLogger(__name__)

def my_function():
    logger.debug("Entering function")
    try:
        # Code here
        logger.info("Operation successful")
    except Exception as e:
        logger.error(f"Operation failed: {str(e)}", exc_info=True)
```

---

### **4. Advanced Features**

#### **Rotating Log Files**
```python
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    'app.log',
    maxBytes=5*1024*1024,  # 5MB
    backupCount=3
)
logger.addHandler(handler)
```

#### **Timed Rotation**
```python
from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler(
    'app.log',
    when='midnight',
    backupCount=7
)
logger.addHandler(handler)
```

#### **Capture Warnings**
```python
logging.captureWarnings(True)  # Redirect warnings to logging system
```

#### **Exception Logging**
```python
try:
    risky_operation()
except Exception:
    logger.exception("Context message")  # Automatically includes stack trace
```

---

### **5. Example Output**
With your configuration, logs will appear as:
```
24-07-2023 14:30:45 - module3 - INFO - Info message for module3
24-07-2023 14:30:45 - module1 - DEBUG - Debug message for module1
24-07-2023 14:30:45 - module2 - WARNING - Warning message for module2
24-07-2023 14:30:45 - module3 - ERROR - Error message for module3
```

---

### **6. Common Pitfalls & Fixes**

| Issue | Solution |
|-------|----------|
| No logs appearing | Check `logger.setLevel()` and handler levels |
| Duplicate logs | Ensure `logging.basicConfig()` is called once |
| Missing stack traces | Use `logger.exception()` or `exc_info=True` |
| Performance impact | Use `isEnabledFor()`: `logger.isEnabledFor(logging.DEBUG)` |

---

### **7. Recommended Structure**
```
my_app/
├── __init__.py
├── utils/
│   ├── __init__.py
│   └── helpers.py  # Uses logging.getLogger(__name__)
└── logging_config.py  # Centralized configuration
```

Would you like me to elaborate on any specific aspect (e.g., distributed system logging, JSON formatting, or integration with monitoring tools)?