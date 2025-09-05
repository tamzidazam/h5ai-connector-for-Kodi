# -*- coding: utf-8 -*-
#
# Kodi h5ai Connector
#
# --- Imports ---
import sys
from urllib.parse import parse_qs, quote_plus, urljoin, parse_qsl
import xbmcgui
import xbmcplugin
import requests
from bs4 import BeautifulSoup
import xbmc
import traceback # Import traceback for detailed error logging

# --- Plugin constants ---
__addon__ = 'h5ai Connector'
__author__ = 'Tamzid Azam Priyo'
__version__ = '1.0.19' # Incremented version

# --- Main plugin class ---
class H5aiClient:
    """
    Main plugin class.
    Handles fetching and parsing of h5ai directory listings.
    """
    def __init__(self, argv):
        """
        Plugin constructor.
        """
        self.base_url = sys.argv[0]
        self.addon_handle = int(sys.argv[1])
        self.args = parse_qs(sys.argv[2][1:])
        xbmc.log(f"[{__addon__}] Started with args: {argv}", level=xbmc.LOGINFO)

    def list_sources(self):
        """
        Lists the configured source URLs from settings as the root directory.
        """
        xbmc.log(f"[{__addon__}] Listing configured sources.", level=xbmc.LOGINFO)
        from resources.lib import settings
        
        # Loop through up to 10 possible sources
        for i in range(1, 11):
            source_name = settings.get_setting(f'source_{i}_name')
            source_url = settings.get_setting(f'source_{i}_url')
            
            # Add the source to the list if it has a name and a valid URL
            if source_name and source_url and source_url != 'http://':
                list_item = xbmcgui.ListItem(label=source_name)
                # Create a URL that tells the addon to list the contents of this source_url
                url = '{0}?action=list&category={1}'.format(
                    self.base_url, quote_plus(source_url)
                )
                xbmcplugin.addDirectoryItem(
                    handle=self.addon_handle,
                    url=url,
                    listitem=list_item,
                    isFolder=True
                )
        
        xbmcplugin.endOfDirectory(self.addon_handle)
        xbmc.log(f"[{__addon__}] Source listing ended.", level=xbmc.LOGINFO)

    def list_directory(self, category_url):
        """
        Lists the contents of a directory from an h5ai instance.

        :param category_url: The URL of the directory to list.
        :type category_url: str
        """
        xbmc.log(f"[{__addon__}] Listing directory: {category_url}", level=xbmc.LOGINFO)
        try:
            # Add a User-Agent header to mimic a browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            # Use requests to fetch the content of the URL
            response = requests.get(category_url, headers=headers, timeout=10)
            response.raise_for_status()  # Raise an exception for bad status codes
            html_content = response.text

            # Use BeautifulSoup to parse the HTML
            soup = BeautifulSoup(html_content, 'html.parser')

            # Grab all links from the body of the page. This is the most generic approach.
            if not soup.body:
                raise ValueError("Could not find body tag in the HTML response.")
            links = soup.body.find_all('a')

            xbmc.log(f"[{__addon__}] Found {len(links)} potential items.", level=xbmc.LOGINFO)

            # A set to keep track of links we've already added to prevent duplicates
            added_hrefs = set()

            for link in links:
                href = link.get('href')
                name = link.text.strip()

                # Filter out irrelevant links
                if not href or href.startswith('?') or not name:
                    continue
                
                # Filter out table headers, parent directory links, and h5ai footer links
                if name in ('Name', 'Last modified', 'Size', 'Description', 'Parent Directory', 'modern browsers', 'powered by h5ai'):
                    continue

                # Use href for duplicate check as it's more reliable
                if href in added_hrefs:
                    continue
                added_hrefs.add(href)

                full_url = urljoin(category_url, href)
                list_item = xbmcgui.ListItem(label=name)
                
                # Check if it's a directory by looking for a trailing slash in the href
                is_directory = href.endswith('/')

                if is_directory:
                    url = '{0}?action=list&category={1}'.format(
                        self.base_url, quote_plus(full_url)
                    )
                    xbmcplugin.addDirectoryItem(
                        handle=self.addon_handle,
                        url=url,
                        listitem=list_item,
                        isFolder=True
                    )
                else:
                    list_item.setProperty('IsPlayable', 'true')
                    xbmcplugin.addDirectoryItem(
                        handle=self.addon_handle,
                        url=full_url,
                        listitem=list_item,
                        isFolder=False
                    )

        except requests.exceptions.RequestException as e:
            error_message = f"Error fetching URL: {e}"
            xbmc.log(f"[{__addon__}] {error_message}", level=xbmc.LOGERROR)
            xbmc.log(traceback.format_exc(), level=xbmc.LOGERROR)
            xbmcgui.Dialog().notification(__addon__, error_message, xbmcgui.NOTIFICATION_ERROR)
        except Exception as e:
            error_message = f"An unexpected error occurred: {e}"
            xbmc.log(f"[{__addon__}] {error_message}", level=xbmc.LOGERROR)
            xbmc.log(traceback.format_exc(), level=xbmc.LOGERROR)
            xbmcgui.Dialog().notification(__addon__, error_message, xbmcgui.NOTIFICATION_ERROR)

        xbmcplugin.endOfDirectory(self.addon_handle)
        xbmc.log(f"[{__addon__}] Directory listing ended.", level=xbmc.LOGINFO)


    def router(self, paramstring):
        """
        Router function that calls other functions
        depending on the provided paramstring
        """
        xbmc.log(f"[{__addon__}] Router called with: {paramstring}", level=xbmc.LOGINFO)
        params = dict(parse_qsl(paramstring))
        if params:
            action = params.get('action')
            if action == 'list':
                self.list_directory(params['category'])
        else:
            # If no action is specified, we list the configured sources
            xbmc.log(f"[{__addon__}] No action specified, listing sources.", level=xbmc.LOGINFO)
            self.list_sources()


if __name__ == '__main__':
    client = H5aiClient(sys.argv)
    client.router(sys.argv[2][1:])

