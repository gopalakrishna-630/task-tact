from services.search_service import SearchService
import sys

print("by_id 'TT001':", SearchService.by_id("TT001"))
print("by_title 'hi':", SearchService.by_title("hi"))
print("by_category 'work':", SearchService.by_category("work"))
print("by_priority 'low':", SearchService.by_priority("low"))
print("by_status 'pending':", SearchService.by_status("pending"))
print("by_tag 'any':", SearchService.by_tag("any"))
print("search_all 'hi':", SearchService.search_all("hi"))
