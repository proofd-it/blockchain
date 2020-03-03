/**
 * Track the trade of a commodity from one trader to another
 * @param {org.abdn.ac.uk.Delivery} delivery - the trade to be processed
 * @transaction
 */
async function deliverCommodity(delivery) {
    delivery.commodity.owner = delivery.newOwner;
    delivery.commodity.status = delivery.status;
    delivery.commodity.complianceReport = delivery.complianceReport;
    let assetRegistry = await getAssetRegistry('org.abdn.ac.uk.Commodity');
    await assetRegistry.update(delivery.commodity);
}
