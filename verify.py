from playwright.sync_api import sync_playwright, expect

def run_verification(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:8000")

    # Wait for the loading indicator to disappear
    loading_indicator = page.locator("#loading")

    try:
        expect(loading_indicator).to_be_hidden(timeout=10000) # 10 second timeout
        print("Verification successful: Loading indicator disappeared.")
    except Exception as e:
        print(f"Verification failed: {e}")

    page.screenshot(path="verification.png")
    browser.close()

with sync_playwright() as playwright:
    run_verification(playwright)
