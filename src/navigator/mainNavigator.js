import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import UserProfile200877Navigator from '../features/UserProfile200877/navigator';
import Tutorial200876Navigator from '../features/Tutorial200876/navigator';
import NotificationList200848Navigator from '../features/NotificationList200848/navigator';
import Settings200847Navigator from '../features/Settings200847/navigator';
import Settings200839Navigator from '../features/Settings200839/navigator';
import UserProfile200837Navigator from '../features/UserProfile200837/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
UserProfile200877: { screen: UserProfile200877Navigator },
Tutorial200876: { screen: Tutorial200876Navigator },
NotificationList200848: { screen: NotificationList200848Navigator },
Settings200847: { screen: Settings200847Navigator },
Settings200839: { screen: Settings200839Navigator },
UserProfile200837: { screen: UserProfile200837Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
